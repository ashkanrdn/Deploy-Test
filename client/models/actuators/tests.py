import unittest

from irrigation import Irrigation
from air import Air
from lighting import LedMain
from config import *
import time


class IrrigationTest:
    def setUp(self):
        self.irrigation_unit = Irrigation(main_pump_gpio=IrrigationGPIOs.MAIN_PUMP,
                                          water_sol_gpio=IrrigationGPIOs.WATER_SOL,
                                          tank_switch_sol_gpio=IrrigationGPIOs.TANK_SWITCH,
                                          nutr_sol_gpio=IrrigationGPIOs.NUTR_SOL,
                                          levels_sol_gpios=[gpio.value for gpio in LevelSolenoidsGPIOs],
                                          main_tank_empty_gpio=TankSensorGPIOs.MAIN_TANK_SENSOR_EMPTY,
                                          main_tank_full_gpio=TankSensorGPIOs.MAIN_TANK_SENSOR_FULL,
                                          drain_tank_empty_gpio=TankSensorGPIOs.DRAIN_TANK_SENSOR_EMPTY,
                                          drain_tank_full_gpio=TankSensorGPIOs.DRAIN_TANK_SENSOR_FULL)

    def test_irrigation_waterCycle(self):
        self.irrigation_unit.run_cycle(duration=5)


class LightingTest:
    def setUp(self):
        self.lighting_unit = LedMain(LightingGPIOs.MAIN_POWER, LightingGPIOs.MAIN_DIM,
                                     LightingGPIOs.SUPP_ONE_DIM, LightingGPIOs.SUPP_TWO_DIM)

    def test_dimming(self):
        # self.lighting_unit.power_on()
        # self.lighting_unit.dim(0.9, 0, 0)
        # time.sleep(5)
        # self.lighting_unit.dim(main_dim=.45)
        # time.sleep(5)
        self.lighting_unit.power_on()
        time.sleep(5)
        print('dim')


        self.lighting_unit.power_on()

        time.sleep(5)
        # print('dim')
        # time.sleep(5)

        self.lighting_unit.power_off()

        # self.lighting_unit.dim(main_dim=0)


class FanTest(unittest.TestCase):
    def setUp(self):
        self.air_unit = Air(AIR_MAIN_GPIO)

    def test_fan_on_off(self):
        self.air_unit.on()
        time.sleep(2)
        self.air_unit.off()
        time.sleep(0.5)



# irrigation_test = IrrigationTest()
# irrigation_test.setUp()
# # irrigation_test.test_irrigation_waterCycle()
# irrigation_test.irrigation_unit.sol_check()
# # lighting_test = LightingTest()
# # lighting_test.setUp()
# # lighting_test.test_dimming()