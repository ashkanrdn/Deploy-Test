import unittest
from fan import AIR
from config import FanGPIOs
import time

class FanTest(unittest.TestCase):
    def setUp(self):
        self.air_units = [
        AIR(gpioAIRMain=FanGPIOs.FanOne.value),
        AIR(gpioAIRMain=FanGPIOs.FanTwo.value),
        AIR(gpioAIRMain=FanGPIOs.FanThree.value)
        ]

    
    def fan_on_off_test(self):
        for air_unit in self.air_units:
            air_unit.On()
            time.sleep(2)
            air_unit.Off()
            time.sleep(0.5)

fan_test_unit = FanTest()
fan_test_unit.setUp()
fan_test_unit.fan_on_off_test()