# TODO write tests with mocks so we can test without the sensors in hand

from unittest import TestCase
from sensor import Co2Sensor
from config import CO2_SENSORS_TSLS
import board
import adafruit_tca9548a


class TestC02Sensor(TestCase):
    def setUp(self):
                # Create I2C bus as normal
        i2c = board.I2C()  # uses board.SCL and board.SDA
        # Create thSensore TCA9548A object and give it the I2C bus
        tca = adafruit_tca9548a.TCA9548A(i2c)
        self.sensors = [Co2Sensor(name=name, sensor_tsl=tca[tsl]) for name, tsl in CO2_SENSORS_TSLS.items()]

    def test_sensor(self):
        for sensor in self.sensors:
            sensor_date = sensor.read_sensor()
            print(sensor_date)

test_object = TestC02Sensor()
test_object.setUp()
test_object.test_sensor()