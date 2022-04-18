import unittest

from .irrigation import Irrigation
from .config import IrrigationGPIOs


class IrrigationTest(unittest.TestCase):
    def setUp(self):
        self.irrigation_unit = Irrigation(main_pump_gpio=IrrigationGPIOs.MAIN_PUMP.value,
                                          lvl1_sol_gpio=IrrigationGPIOs.LEVEL_ONE_SOL.value)

    def test_irrigation_waterCycle(self):
        self.irrigation_unit.run_water_cycle(duration=5)


# irrigation_tester = IrrigationTest()
# irrigation_tester.setUp()
# irrigation_tester.test_irrigation_waterCycle()