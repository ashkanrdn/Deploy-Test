import time
import logging
from apscheduler.schedulers.background import BackgroundScheduler

from datetime import datetime
from typing import Dict, List
from csv import DictWriter
from ..sensors.sensors_controller import sensor_controller
from ..actuators.actuator_controller import actuator_controller
from ..actuators.config import *

logging.basicConfig(filename='amps_v2.log',
                    format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO)


class ActuatorScheduler:

    def __init__(self):
        # converting times strings to time objects
        # TODO get this data from database instead of reading locally

        self.scheduler = BackgroundScheduler()
        self.immediate_scheduler = BackgroundScheduler()
        self.irrigation_schedule = []
        self.lighting_schedule = []
        self.air_schedule = []
        irrigation_schedule = [(datetime.strptime(cycle_time, "%H:%M:%S"), duration) for cycle_time, duration in
                               IRRIGATION_SCHEDULE]
        lighting_schedule = [(datetime.strptime(time_on, "%H:%M:%S"), datetime.strptime(time_off, "%H:%M:%S"))
                             for time_on, time_off in LIGHTING_SCHEDULE]
        air_schedule = [(datetime.strptime(time_on, "%H:%M:%S"), datetime.strptime(time_off, "%H:%M:%S"))
                        for time_on, time_off in AIR_SCHEDULE]

        self.add_irrigation_jobs(irrigation_schedule=irrigation_schedule)
        self.add_air_jobs(air_schedule=air_schedule)
        self.add_lighting_jobs(lighting_schedule=lighting_schedule)
        # self.create_other_jobs()
        self.status = False
        self.initiated = False

    def reinitiate_state(self):
        current_time = datetime.now().time()
        logging.info("schedule starts")

        for scheduled_window in self.air_schedule:
            if scheduled_window[0].time() <= current_time <= scheduled_window[1].time():
                actuator_controller.air_controller.on()
                logging.info('fans on')
                break
        else:
            actuator_controller.air_controller.off()
            logging.info('fans off')

        for scheduled_window in self.lighting_schedule:
            if scheduled_window[0].time() <= current_time <= scheduled_window[1].time():
                actuator_controller.led_controller.dim()
                logging.info('lights on')
                break
        else:
            actuator_controller.led_controller.dim(main_dim=0, supp1_dim=0, supp2_dim=0)
            logging.info('lights off')

    @staticmethod
    def turn_off_actuators():
        actuator_controller.air_controller.off()
        actuator_controller.led_controller.power_off()

    @staticmethod
    def valid_schedule(time_schedule: List):
        """
        checks if there are overlaps in the schedule and if the window is valid or not
        """
        time_schedule.sort()
        for i in range(len(time_schedule) - 1):
            if time_schedule[i][0] >= time_schedule[i][1]:
                raise Exception(
                    f'This time window is not valid: {time_schedule[0][0].time()} to {time_schedule[0][1].time()}')
            for j in range(i + 1, len(time_schedule)):
                if time_schedule[i][1] > time_schedule[j][0]:
                    raise Exception(
                        f'This two time windows have overlaps: {time_schedule[0][0].time()} to {time_schedule[0][1].time()} and {time_schedule[j][0].time()} to {time_schedule[j][1].time()}')

    def run_immediate_irrigation_job(self, duration):
        self.immediate_scheduler.add_job(lambda :actuator_controller.irrigation_controller.run_cycle(duration=duration))

    def add_irrigation_jobs(self, irrigation_schedule: List):
        irrigation_jobs = [
            self.scheduler.add_job(lambda: actuator_controller.irrigation_controller.run_cycle(duration=duration),
                                   'cron',
                                   id=f'IRG-{irrigation_time.time()}', hour=irrigation_time.hour,
                                   minute=irrigation_time.minute) for
            irrigation_time, duration in irrigation_schedule]
        self.irrigation_schedule += irrigation_schedule
        self.irrigation_schedule.sort()

        return irrigation_jobs

    def add_air_jobs(self, air_schedule):
        self.valid_schedule(time_schedule=self.air_schedule + air_schedule)
        air_on_jobs = [
            self.scheduler.add_job(actuator_controller.air_controller.on, 'cron', hour=air_on_time.hour,
                                   id=f'AIR-ON-{air_on_time.time()}',
                                   minute=air_on_time.minute)
            for air_on_time, air_off_time in air_schedule
        ]
        air_off_jobs = [
            self.scheduler.add_job(actuator_controller.air_controller.off, 'cron', hour=air_off_time.hour,
                                   id=f'AIR-OFF-{air_off_time.time()}',
                                   minute=air_off_time.minute)
            for air_on_time, air_off_time in air_schedule
        ]
        self.air_schedule += air_schedule
        self.air_schedule.sort()
        return air_on_jobs + air_off_jobs

    def add_lighting_jobs(self, lighting_schedule):
        self.valid_schedule(time_schedule=self.lighting_schedule + lighting_schedule)

        lighting_on_jobs = [
            self.scheduler.add_job(actuator_controller.led_controller.dim, 'cron',
                                   id=f'LIGHT-ON-{lighting_on_time.time()}',
                                   hour=lighting_on_time.hour, minute=lighting_on_time.minute) for
            lighting_on_time, lighting_off_time in lighting_schedule]
        lighting_off_jobs = [
            self.scheduler.add_job(actuator_controller.led_controller.off, 'cron',
                                   id=f'LIGHT-OFF-{lighting_off_time.time()}',
                                   hour=lighting_off_time.hour, minute=lighting_off_time.minute) for
            lighting_on_time, lighting_off_time in lighting_schedule]

        self.lighting_schedule += lighting_schedule
        self.lighting_schedule.sort()
        return lighting_on_jobs + lighting_off_jobs

    def remove_irrigation_job(self, scheduled_time):

        try:

            job_id = f'IRG-{scheduled_time}'
            scheduled_datetime = datetime.strptime(scheduled_time, "%H:%M:%S")

            self.scheduler.remove_job(job_id)
            for job_time in self.irrigation_schedule:
                if time == scheduled_datetime:
                    self.irrigation_schedule.remove(job_time)
                    break
            if self.status:
                self.reinitiate_state()

        except Exception as e:
            logging.error(e)
            raise e

    def remove_window_jobs(self, scheduled_window, job_type):
        scheduled_list = self.lighting_schedule if job_type == 'LIGHT' else self.air_schedule

        on_time, off_time = [datetime.strptime(scheduled_time, "%H:%M:%S") for scheduled_time in
                             scheduled_window.split('-')]
        on_id = f'{job_type}-ON-{on_time.time()}'
        off_id = f'{job_type}-OFF-{off_time.time()}'
        for i, window in enumerate(scheduled_list):
            if window[0] == on_time and window[1] == off_time:
                try:
                    scheduled_list.pop(i)
                    self.scheduler.remove_job(on_id)
                    self.scheduler.remove_job(off_id)

                    break

                except Exception as e:
                    logging.error(e)
                    raise e
        if self.status:
            self.reinitiate_state()

    # def create_other_jobs(self):
    #     self.scheduler.add_job(actuator_controller.sol_check, 'interval', minutes=30)

    def start(self):
        if not self.status:
            self.reinitiate_state()
            self.scheduler.start() if not self.initiated else self.scheduler.resume()
            self.status = True
            self.initiated = True

    def pause(self):
        if self.status:
            self.scheduler.pause()
            self.turn_off_actuators()
            self.status = False


actuator_scheduler = ActuatorScheduler()
