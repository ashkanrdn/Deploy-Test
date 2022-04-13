import unittest
from ..actuators.fan import Fan
from ..actuators.config import FanGPIOs
import time


class FanTest(unittest.TestCase):
    def setUp(self):
        self.air_units = [
            Fan(fan_gpio=FanGPIOs.FAN_ONE.value),
            Fan(fan_gpio=FanGPIOs.FAN_TWO.value),
            Fan(fan_gpio=FanGPIOs.FAN_THREE.value)
        ]

    def test_fan_on_off(self):
        for air_unit in self.air_units:
            air_unit.on()
            time.sleep(2)
            air_unit.off()
            time.sleep(0.5)

