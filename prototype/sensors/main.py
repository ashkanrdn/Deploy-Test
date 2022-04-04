import time
import logging
from sensors_controller import SensorReader
from config import SLEEPING_TIME_IN_SECONDS

if __name__ == "__main__":
    sensor_reader = SensorReader()
    while True:
        samples = sensor_reader.run()
        print(samples)
        time.sleep(SLEEPING_TIME_IN_SECONDS)
