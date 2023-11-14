from datetime import datetime
from typing import List, Dict
import adafruit_tca9548a
import board

from config import *


class SensorController:
    def __init__(self):
        # Create I2C bus as normal
        i2c = board.I2C()  # uses board.SCL and board.SDA
        # Create the Sensor TCA9548A object and give it the I2C bus
        tca = adafruit_tca9548a.TCA9548A(i2c)
        self.sensors = {}
        self.setup_sensors(tca)

    def setup_sensors(self, tca):
        """self.sensors = {
            AirSensorType: list of sensors with type AirSenor,
            SoilSensorType: list of sensors with type SoilSensor
            ...
        }"""

        for sensor_type in SensorsTypes:
            self.sensors[sensor_type] = [sensor_type.value(sensor_tsl=tca[tsl], name=name) for tsl, name in
                                         TSLS[sensor_type]]

    def read_sensors(self):
        samples = {}
        for sensors in self.sensors:
            for sensor in sensors:
                try:
                    sample = sensor.read_sensor()
                    for feature in sample.keys():
                        samples[f"{sensor.name.lower()}_{feature}"] = sample[feature]
                except Exception as e:
                    e.message = f"{self.name}_{e.message}"
                    raise e
            return samples

    def run(self):
        timestamp = datetime.now().strftime('%y-%m-%d,%H:%M:%S,')
        samples = self.read_sensors()
        samples['timestamp'] = timestamp
        return samples


sensor_controller = SensorController()
