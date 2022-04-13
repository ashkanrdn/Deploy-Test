import unittest
from ..actuators.lighting import Led
from ..actuators.config import LightGPIOs
import time


class LightingTest(unittest.TestCase):
    def setUp(self):
        self.lighting_unit = Led(gpioDim=LightGPIOs.MAIN_LED)

    def test_dimming(self):
        self.lighting_unit.dim(1)
        time.sleep(5)
        self.lighting_unit.dim(0.5)
        time.sleep(5)
        self.lighting_unit.dim(0)

