import unittest
from sensors.sensors_controller import SensorReader

class SensorTest(unittest.TestCaes):
    def setUp(self):
        self.sensor_reader = SensorReader()

    def test_air_sensors_output(self):
        for sensor in self.sensor_reader.air_sensors:
            sample = sensor.read_sensor()
            self.assert

    def test_soil_sensors_output(self):
        pass

    def test_co2_sensors_output(self):
    pass

    def test_voc_sensors_output(self):
    pass

    def test_light_sensors_output(self):
    pass