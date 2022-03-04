import time
from sensors_controller import SensorReader
from config import SLEEPING_TIME_IN_SECONDS

if __name__ == "__main__":
    sensor_reader = SensorReader()
    while True:
        sensor_reader.run()
        time.sleep(SLEEPING_TIME_IN_SECONDS)
