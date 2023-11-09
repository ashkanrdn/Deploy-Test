from .air import Air
from .arm import Arm
from .irrigation import Irrigation
from .lighting import LedMain
from .config import *
import logging


class ActuatorController:
    def __init__(self):
        self.led_controller = LedMain(LightingGPIOs.MAIN_POWER, 

        )

        self.irrigation_controller = Irrigation(
                                        water_sol_gpio=IrrigationGPIOs.WATER_SOL,
                                        tank_switch_sol_gpio=IrrigationGPIOs.TANK_SWITCH,
                                        nutr_sol_gpio=IrrigationGPIOs.NUTR_SOL,
                                        levels_sol_gpios=[gpio.value for gpio in LevelSolenoidsGPIOs],
                                        pressure_relief_gpio=IrrigationGPIOs.PRESS_RELIEF)

        self.air_controller = Air(AIR_MAIN_GPIO)

    def check_tank(self):
        if self.irrigation_controller.tank_full():
            self.led_controller.panic_mode()

actuator_controller = ActuatorController()