import unittest
from .lighting import Led
from .config import LightGPIOs
import time


class LightingTest(unittest.TestCase):
    def setUp(self):
        self.lighting_unit = Led(dim_gpio=LightGPIOs.MAIN_LED.value)

    def test_dimming(self):
        self.lighting_unit.dim(1)
        time.sleep(5)
        self.lighting_unit.dim(0.5)
        time.sleep(5)
        self.lighting_unit.dim(0)

# light_tester = LightingTest()
# light_tester.setUp()
# light_tester.test_dimming()
