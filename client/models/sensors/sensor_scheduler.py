
import logging
from apscheduler.schedulers.background import BackgroundScheduler

from typing import Dict, List
from csv import DictWriter
from ..sensors.sensors_controller import sensor_controller


logging.basicConfig(filename='amps_v2.log',
                    format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO)


class SensorScheduler:

    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.status = False
        self.initiated = False

    @staticmethod
    def store_samples(samples: Dict, file_name: str):
        with open(file_name, 'a') as csv_file:
            fields = samples.keys()
            dict_writer = DictWriter(csv_file, fields)
            dict_writer.writerow(samples)
            csv_file.close()

    @staticmethod
    def sensor_read_and_publish(self):
        samples = sensor_controller.read_sensors()
        print(samples)
        logging.info(samples)

    def create_sensor_job(self):
        self.scheduler.add_job(self.sensor_read_and_publish, 'interval', seconds=3)

    def start(self):
        if not self.status:
            self.scheduler.start() if not self.initiated else self.scheduler.resume()
            self.status = True
            self.initiated = True

    def pause(self):
        if self.status:
            self.scheduler.pause()
            self.status = False


sensor_scheduler = SensorScheduler()
