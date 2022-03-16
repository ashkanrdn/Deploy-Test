from datetime import datetime
from typing import List, Dict

import adafruit_tca9548a
import board

from sensor import Sensor, AirSensor, SoilSensor, Co2Sensor, VoCSensor
from config import AIR_SENSORS_TSLS, SOIL_SENSORS_TSLS, CO2_SENSORS_TSLS, VOC_SENSORS_TSLS


class SensorReader:
    air_sensors: List[Sensor]
    soil_sensors: List[Sensor]
    voc_sensors: List[Sensor]
    co2_sensors: List[Sensor]

    def __init__(self):
        # Create I2C bus as normal
        i2c = board.I2C()  # uses board.SCL and board.SDA
        # Create thSensore TCA9548A object and give it the I2C bus
        tca = adafruit_tca9548a.TCA9548A(i2c)
        self.air_sensors = [
            AirSensor(sensor_tsl=tca[tsl], name=name) for name, tsl in AIR_SENSORS_TSLS.items()
        ]
        self.soil_sensors = [
            SoilSensor(sensor_tsl=tca[tsl], name=name) for name, tsl in
            SOIL_SENSORS_TSLS.items()]
        self.co2_sensors = [
            AirSensor(sensor_tsl=tca[tsl], name=name) for name, tsl in CO2_SENSORS_TSLS.items()]
        self.voc_sensors = [
            VoCSensor(sensor_tsl=tca[tsl], name=name) for name, tsl in
            VOC_SENSORS_TSLS.items()]

    def read_sensors(self):
        samples = {}
        sensors = [
            *self.air_sensors,
            *self.soil_sensors,
            *self.co2_sensors,
            *self.voc_sensors
        ]
        for sensor in sensors:
            sample = sensor.read_sensor()
            for feature in sample.keys():
                samples[sensor.name + feature] = sample[feature]

        return samples

    def run(self) -> Dict:
        timestamp = datetime.now().strftime('%y-%m-%d,%H:%M:%S,')
        samples = self.read_sensors()
        data = {
            "timestamp": timestamp,
            **samples
        }
        return samples
