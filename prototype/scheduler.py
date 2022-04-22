import time
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from sensors.sensors_controller import SensorReader
from sensors.config import SLEEPING_TIME_IN_SECONDS, SampleFileName
from actuators.actuator_repository import ActuatorRepository
from actuators.config import *
from csv import DictWriter


class Scheduler:
    # converting times strings to time objects
    irrigation_schedule = [datetime.strptime(time_, "%H:%M:%S") for time_ in IRRIGATION_SCHEDULE]
    lighting_schedule = [(datetime.strptime(time_on, "%H:%M:%S"), datetime.strptime(time_off, "%H:%M:%S")) for
                         time_on, time_off in LIGHTING_SCHEDULE]
    ventilation_schedule = [(datetime.strptime(time_on, "%H:%M:%S"), datetime.strptime(time_off, "%H:%M:%S")) for
                            time_on, time_off in AIR_SCHEDULE]

    # setup sensors and actuators
    sensor_reader = SensorReader()

    actuator_repo = ActuatorRepository()

    @staticmethod
    def in_time_schedule(current_time, scheduled_times: List[datetime.time], time_window=SLEEPING_TIME_IN_SECONDS):
        for scheduled_time in scheduled_times:
            if scheduled_time.time() <= current_time <= (scheduled_time + timedelta(seconds=time_window)).time():
                return True
        return False

    @staticmethod
    def in_time_schedule_window(current_time, scheduled_windows: List[Tuple[datetime.time]]):
        for scheduled_window in scheduled_windows:
            if scheduled_window[0].time() <= current_time <= scheduled_window[1].time():
                return True
        return False

    def run_actuators(self):
        current_time = datetime.now().time()

        if self.in_time_schedule(current_time, self.irrigation_schedule):
            self.actuator_repo.irrigation.run_water_cycle(duration=WATER_CYCLE_DURATION)

        if self.in_time_schedule_window(current_time, self.ventilation_schedule):
            [fan.on() for fan in self.actuator_repo.fans]
        else:
            [fan.off() for fan in self.actuator_repo.fans]

        if self.in_time_schedule_window(current_time, self.lighting_schedule):

            self.actuator_repo.main_led.on()
        else:
            self.actuator_repo.main_led.off()

    def setup_sample_file(self, samples: Dict, file_name: str):
        with open(file_name, 'a') as csv_file:
            fields = samples.keys()
            dict_writer = DictWriter(csv_file, fields)
            header_row = {field: field for field in fields}
            dict_writer.writerow(header_row)
            csv_file.close()

    def store_samples(self, samples: Dict, file_name: str):
        with open(file_name, 'a') as csv_file:
            fields = samples.keys()
            dict_writer = DictWriter(csv_file, fields)
            dict_writer.writerow(samples)
            csv_file.close()

    # def update_irrigation_schedule(self, irrigation_schedule):
    #     self.irrigation_schedule = irrigation_schedule
    #     print('irrigation schedule updated to', irrigation_schedule)

    # def update_lighting_schedule(self, lighting_schedule):
    #     self.lighting_schedule = lighting_schedule
    #     print('lighting schedule updated to', lighting_schedule)

    # def update_ventilation_schedule(self, ventilation_schedule):
    #     self.ventilation_schedule = ventilation_schedule
    #     print('ventilation schedule updated to', ventilation_schedule)

    def run(self):
        while True:
            samples = self.sensor_reader.run()
            print(samples)  # TODO replace with pymongo
            self.store_samples(samples, SampleFileName.v3.value)
            self.run_actuators()
            time.sleep(SLEEPING_TIME_IN_SECONDS)


if __name__ == "__main__":
    Scheduler().run()
