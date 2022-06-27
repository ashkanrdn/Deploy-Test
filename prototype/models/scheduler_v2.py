import time
import logging
from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime
from typing import Dict, List, Tuple
from csv import DictWriter

from sensors.sensors_controller import sensor_reader
from actuators.actuator_repository import actuator_repository
from actuators.config import *

logging.basicConfig(filename='amps_v2.log',
                    format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO)


class SchedulerV2:

    def __init__(self):
        # converting times strings to time objects
        # TODO get this data from database instead of reading locally

        self.scheduler = BackgroundScheduler()
        self.irrigation_schedule = [datetime.strptime(time_, "%H:%M:%S") for time_ in IRRIGATION_SCHEDULE]
        self.lighting_schedule = [(datetime.strptime(time_on, "%H:%M:%S"), datetime.strptime(time_off, "%H:%M:%S"))
                                  for time_on, time_off in LIGHTING_SCHEDULE]
        self.air_schedule = [(datetime.strptime(time_on, "%H:%M:%S"), datetime.strptime(time_off, "%H:%M:%S"))
                             for time_on, time_off in AIR_SCHEDULE]

        self.irrigation_jobs = self.create_irrigation_jobs(irrigation_schedule=self.irrigation_schedule)
        self.air_jobs = self.create_air_jobs(air_schedule=self.air_schedule)
        self.lighting_jobs = self.create_lighting_jobs(lighting_schedule=self.lighting_schedule)
        self.sensor_reader_job = self.create_sensor_job()
        self.status = False
        self.initiated = False

    def initial_state(self):
        current_time = datetime.now().time()
        logging.info("schedule starts")

        for scheduled_window in self.air_schedule:
            if scheduled_window[0].time() <= current_time <= scheduled_window[1].time():
                actuator_repository.fans_on()
                logging.info('fans on')
                break

        for scheduled_window in self.lighting_schedule:
            if scheduled_window[0].time() <= current_time <= scheduled_window[1].time():
                actuator_repository.main_led.on()
                logging.info('lights on')
                break

    def turn_off_actuators(self):
        actuator_repository.fans_off()
        actuator_repository.main_led.off()

    def create_irrigation_jobs(self, irrigation_schedule: List[datetime]):
        irrigation_jobs = [self.scheduler.add_job(actuator_repository.run_water_cycle, 'cron',
                                                  hour=irrigation_time.hour, minute=irrigation_time.minute) for
                           irrigation_time in irrigation_schedule]

        return irrigation_jobs

    def create_air_jobs(self, air_schedule):
        air_on_jobs = [
            self.scheduler.add_job(actuator_repository.fans_on, 'cron', hour=air_on_time.hour,
                                   minute=air_on_time.minute)
            for air_on_time, air_off_time in air_schedule
        ]
        air_off_jobs = [
            self.scheduler.add_job(actuator_repository.fans_off, 'cron', hour=air_off_time.hour,
                                   minute=air_off_time.minute)
            for air_on_time, air_off_time in air_schedule
        ]

        return air_on_jobs + air_off_jobs

    def create_lighting_jobs(self, lighting_schedule):
        lighting_on_jobs = [self.scheduler.add_job(actuator_repository.lights_on, 'cron',
                                                   hour=lighting_on_time.hour, minute=lighting_on_time.minute) for
                            lighting_on_time, lighting_off_time in lighting_schedule]
        lighting_off_jobs = [self.scheduler.add_job(actuator_repository.lights_off, 'cron',
                                                    hour=lighting_off_time.hour, minute=lighting_off_time.minute) for
                             lighting_on_time, lighting_off_time in lighting_schedule]

        return lighting_on_jobs + lighting_off_jobs

    def sensor_read_and_publish(self):
        samples = sensor_reader.read_sensors()
        print(samples)
        logging.info(samples)

    def create_sensor_job(self):
        return self.scheduler.add_job(self.sensor_read_and_publish, 'interval', seconds=3)

    def store_samples(self, samples: Dict, file_name: str):
        with open(file_name, 'a') as csv_file:
            fields = samples.keys()
            dict_writer = DictWriter(csv_file, fields)
            dict_writer.writerow(samples)
            csv_file.close()

    def start(self):
        if not self.status:
            self.initial_state()
            self.scheduler.start() if not self.initiated else self.scheduler.resume()
            self.status = True
            self.initiated = True

        
        while True:
            pass

    def pause(self):
        if self.status:
            self.scheduler.pause()
            self.turn_off_actuators()
            self.status = False

scheduler_v2 = SchedulerV2()
scheduler_v2.start()
