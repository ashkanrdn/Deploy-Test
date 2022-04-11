import unittest
from actuators.irrigation import Irrigation
from actuators.config import IrrigationGPIOs

class IrrigationTest(unittest.TestCase):
    def setUp(self):
        self.irrigation_unit = Irrigation(gpioIRGMainPump=IrrigationGPIOs.MainPump,
                                     gpioIRGlvl1Sol=IrrigationGPIOs.Lvl1Sol)
    
    def irrigation_waterCycle_test(self):
        self.irrigation_unit.waterCycle(cycleTime=5)