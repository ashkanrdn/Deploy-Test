import unittest
print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__,__name__,str(__package__)))

from prototype.actuators.irrigation import Irrigation
from prototype.actuators.config import IrrigationGPIOs


class IrrigationTest(unittest.TestCase):
    def setUp(self):
        self.irrigation_unit = Irrigation(main_pump_gpio=IrrigationGPIOs.MAIN_PUMP,
                                          lvl1_sol_gpio=IrrigationGPIOs.LEVEL_ONE_SOL)

    def test_irrigation_waterCycle(self):
        self.irrigation_unit.run_water_cycle(cycleTime=5)
