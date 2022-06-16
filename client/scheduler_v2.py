import time
import asyncio

from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from csv import DictWriter

from sensors.sensors_controller import SensorController
from appConfig import SENSOR_CONTROLLER_SLEEPING_TIME
from actuators.actuator_controller import ActuatorController
from actuators.config import *
from logger import logger


class Scheduler:

    def __init__(self):
        # converting times strings to time objects
        # TODO get this data from database instead of reading locally
        self.irrigation_schedule = [datetime.strptime(time_, "%H:%M:%S") for time_ in IRRIGATION_SCHEDULE]
        self.lighting_schedule = [(datetime.strptime(time_on, "%H:%M:%S"), datetime.strptime(time_off, "%H:%M:%S")) for
                                  time_on, time_off in LIGHTING_SCHEDULE]
        self.ventilation_schedule = [(datetime.strptime(time_on, "%H:%M:%S"), datetime.strptime(time_off, "%H:%M:%S"))
                                     for
                                     time_on, time_off in AIR_SCHEDULE]

        self.lights_on_times = [on for on, off in self.lighting_schedule]
        self.lights_off_times = [off for on, off in self.lighting_schedule]
        self.fans_on_times = [on for on, off in self.ventilation_schedule]
        self.fans_off_times = [off for on, off in self.ventilation_schedule]
        # setup sensors and actuators
        self.sensor_controller = SensorController()

        self.actuator_controller = ActuatorController()

    @staticmethod
    def in_time_schedule(current_time: datetime.time, scheduled_times: List[datetime], time_window):
        for scheduled_time in scheduled_times:
            if scheduled_time.time() <= current_time <= (scheduled_time + time_window).time():
                return True
        return False

    @staticmethod
    def in_time_schedule_window(current_time: datetime.time, scheduled_windows: List[Tuple[datetime, datetime]]):
        for scheduled_window in scheduled_windows:
            if scheduled_window[0].time() <= current_time <= scheduled_window[1].time():
                return True
        return False

    def resume_schedule(self, last_cycle_duration):
        current_time = datetime.now().time()

        if self.in_time_schedule(current_time, scheduled_times=self.lights_on_times, time_window=last_cycle_duration):
            self.actuator_controller.led_controller.on()
            logger.info('lights on')

        elif self.in_time_schedule(current_time, scheduled_times=self.lights_off_times,
                                   time_window=last_cycle_duration):
            self.actuator_controller.led_controller.off()
            logger.info('lights off')

        if self.in_time_schedule(current_time, scheduled_times=self.fans_on_times, time_window=last_cycle_duration):
            self.actuator_controller.air_controller.on()
            logger.info('air on')
        elif self.in_time_schedule(current_time, scheduled_times=self.fans_off_times, time_window=last_cycle_duration):
            self.actuator_controller.air_controller.on()
            logger.info('air off')

        if self.in_time_schedule(current_time, self.irrigation_schedule):
            logger.info("water cycle running")
            self.actuator_controller.irrigation_controller.run_water_cycle()

        # self.actuator_controller.irrigation.sol_check()

    def start_schedule(self):
        current_time = datetime.now().time()
        logger.info("schedule starts")

        if self.in_time_schedule_window(current_time, self.ventilation_schedule):
            [fan.on() for fan in self.actuator_controller.fans]
            logger.info('fans on')

        else:
            [fan.off() for fan in self.actuator_controller.fans]
            logger.info('fans off')

        if self.in_time_schedule_window(current_time, self.lighting_schedule):

            self.actuator_controller.main_led.on()
            logger.info('lights on')

        else:
            self.actuator_controller.main_led.off()
            logger.info('lights off')

    def update_irrigation_schedule(self, irrigation_schedule):
        self.irrigation_schedule = irrigation_schedule
        print('irrigation schedule updated to', irrigation_schedule)

    def update_lighting_schedule(self, lighting_schedule):
        self.lighting_schedule = lighting_schedule
        print('lighting schedule updated to', lighting_schedule)

    def update_ventilation_schedule(self, ventilation_schedule):
        self.ventilation_schedule = ventilation_schedule
        print('ventilation schedule updated to', ventilation_schedule)

    def store_samples(self, samples: Dict, file_name: str):
        with open(file_name, 'a') as csv_file:
            fields = samples.keys()
            dict_writer = DictWriter(csv_file, fields)
            dict_writer.writerow(samples)
            csv_file.close()

    async def read_sensors(self):
        samples = self.sensor_controller.read_sensors()
        await asyncio.sleep(SENSOR_CONTROLLER_SLEEPING_TIME)
        return samples

    async def run_actuators(self):
        pass

    async def async_run(self):
        self.start_schedule()
        while True:
            await asyncio.create_task(self.read_sensors())
            await asyncio.create_task(self.run_actuators())


def run(self):
        self.start_schedule()
        time_delta = timedelta(seconds=0)
        while True:
            try:
                cycle_initial_time = datetime.now()
                samples = self.sensor_controller.run()
                print(samples)  # TODO replace with pymongo
                # self.store_samples(samples, SampleFileName.v4.value)
                self.resume_schedule(last_cycle_duration=time_delta)
                time.sleep(SENSOR_CONTROLLER_SLEEPING_TIME)
                cycle_final_time = datetime.now()
                time_delta = cycle_final_time - cycle_initial_time
            except Exception as e:
                logger.error(e)


if __name__ == "__main__":
    Scheduler().run()  # define scheduler globally
