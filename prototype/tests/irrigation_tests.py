import unittest
from ..actuators.irrigation import Irrigation
from ..actuators.config import IrrigationGPIOs


class IrrigationTest(unittest.TestCase):
    def setUp(self):
        self.irrigation_unit = Irrigation(main_pump_gpio=IrrigationGPIOs.MAIN_PUMP,
                                          lvl1_sol_gpio=IrrigationGPIOs.LEVEL_ONE_SOL)

    def test_irrigation_waterCycle(self):
        self.irrigation_unit.run_water_cycle(cycleTime=5)
