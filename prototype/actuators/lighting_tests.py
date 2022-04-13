import unittest
from lighting import LedMain
from config import LightGPIOs
import time

class LightingTest(unittest.TestCase):
    def setUp(self):
        self.lighting_unit = LedMain(gpioDim=LightGPIOs.LEDMain)
    
    def dimming_test(self):
        self.lighting_unit.dim(1)
        time.sleep(5)
        self.lighting_unit.dim(0.5)
        time.sleep(5)
        self.dimming_test.dim(0)    


light_test_unit = LightingTest()
light_test_unit.setUp()
light_test_unit.dimming_test()