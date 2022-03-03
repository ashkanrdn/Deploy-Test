from datetime import datetime
from typing import List

import adafruit_tca9548a
import board

from sensor import Sensor
from config import SensorsTSLs

import adafruit_sht4x
import adafruit_sgp30
import adafruit_sht31d
import adafruit_scd30


class SensorReader:
    air_sensors: List[Sensor]
    soil_sensors: List[Sensor]
    voc_sensors: List[Sensor]
    co2_sensors: List[Sensor]

    def __init__(self):
        # Create I2C bus as normal
        i2c = board.I2C()  # uses board.SCL and board.SDA
        # Create the TCA9548A object and give it the I2C bus
        tca = adafruit_tca9548a.TCA9548A(i2c)
        self.air_sensors = [
            Sensor(sensor_tsl=adafruit_sht4x.SHT4x(tca[SensorsTSLs.AIR_1.value]), name=SensorsTSLs.AIR_1.name),
            Sensor(sensor_tsl=adafruit_sht4x.SHT4x(tca[SensorsTSLs.AIR_2.value]), name=SensorsTSLs.AIR_2.name)]
        self.soil_sensors = [
            Sensor(sensor_tsl=adafruit_sht31d.SHT31D(tca[SensorsTSLs.SOIL_1.value]), name=SensorsTSLs.SOIL_1.name)]
        self.co2_sensors = [
            Sensor(sensor_tsl=adafruit_scd30.SCD30(tca[SensorsTSLs.CO2_1.value]), name=SensorsTSLs.CO2_1.name)]
        self.voc_sensors = [Sensor(sensor_tsl=adafruit_sgp30.Adafruit_SGP30(tca[SensorsTSLs.VOC.value]),
                                   name=SensorsTSLs.VOC.name)]  # voc sensor

    def read_sensors(self):
        samples = {}
        sensors = [
            *self.air_sensors,
            *self.soil_sensors,
            *self.co2_sensors,
            *self.voc_sensors
        ]
        for sensor in sensors:
            samples[sensor.name] = sensor.read_sensor()

        return samples

    def run(self):
        timestamp = datetime.now().strftime('%y-%m-%d,%H:%M:%S,')
        samples = self.read_sensors()
        data = {
            "timestamp": timestamp,
            **samples
        }
        print(data)  # TODO delete
        # send_to_mongo(samples=data)
        # time.sleep(1)