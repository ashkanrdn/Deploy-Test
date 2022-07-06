from typing import List, Dict

import adafruit_scd30
import adafruit_sgp30
import adafruit_sht31d
import adafruit_sht4x
import adafruit_veml7700


class Sensor:
    formatter = '{0:1f}'

    def read_sensor(self):
        raise NotImplementedError


class AirSensor(Sensor):
    def __init__(self, sensor_tsl, name):
        self.name = name
        self.sensor_tsl = adafruit_sht4x.SHT4x(sensor_tsl)
        self.sensor_tsl.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION

    def read_sensor(self) -> Dict:
        temperature, relative_humidity = self.sensor_tsl.measurements
        return {
            "temperature": self.formatter.format(temperature),
            "humidity": self.formatter.format(relative_humidity),
        }


class SoilSensor(Sensor):
    def __init__(self, sensor_tsl, name):
        self.name = name
        self.sensor_tsl = adafruit_sht31d.SHT31D(sensor_tsl)

    def read_sensor(self):
        humidity = self.sensor_tsl.relative_humidity
        self.sensor_tsl.heater = True
        return {
            "humidity": self.formatter.format(humidity),
            "heater_status": self.sensor_tsl.heater
        }


class Co2Sensor(Sensor):
    def __init__(self, sensor_tsl, name):
        self.name = name
        self.sensor_tsl = adafruit_scd30.SCD30(sensor_tsl)

    def read_sensor(self):
        co2, temp, humidity = None, None, None
        if self.sensor_tsl.data_available:
            co2 = self.sensor_tsl.CO2
            temp = self.sensor_tsl.temperature
            humidity = self.sensor_tsl.relative_humidity
        return {"co2": co2, 'temperature': temp, 'humidity': humidity}


class VoCSensor(Sensor):
    def __init__(self, sensor_tsl, name):
        self.name = name
        self.sensor_tsl = adafruit_sgp30.Adafruit_SGP30(sensor_tsl)
        self.sensor_tsl.iaq_init()
        self.sensor_tsl.set_iaq_baseline(0x8973, 0x8AAE)

    def read_sensor(self):
        tvoc = self.sensor_tsl.TVOC
        return {"tvoc": tvoc}


class LightSensor(Sensor):
    def __init__(self, sensor_tsl, name):
        self.name = name
        self.sensor_tsl = adafruit_veml7700.VEML7700(sensor_tsl)

    def read_sensor(self):
        amb_light = self.sensor_tsl.light
        return {"ambient_light": amb_light}