import time
import logging
from sensors.sensors_controller import SensorReader
from sensors.config import SLEEPING_TIME_IN_SECONDS


class Scheduler:
    default_irrigation = [('7:00', 5), ('19:00', 5)]
    default_ventilation = [('7:00', 1000), ('19:00', 1000)]  # TODO change to the correct format
    sensor_reader = SensorReader()

    @staticmethod
    def run():
        while True:
            samples = Scheduler.sensor_reader.run()
            print(samples)  # TODO replace with pymongo
            # TODO check time and if it satisfies the condition, run actuator
            time.sleep(SLEEPING_TIME_IN_SECONDS)


if __name__ == "__main__":
    Scheduler.run()
