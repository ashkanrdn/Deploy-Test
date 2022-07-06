from air import Air
from arm import Arm
from irrigation import Irrigation
from lighting import LedMain
from config import *
import logging


class ActuatorController:
    led_controller = LedMain(LightingGPIOs.MAIN_POWER, LightingGPIOs.MAIN_DIM,
                             LightingGPIOs.SUPP_ONE_DIM, LightingGPIOs.SUPP_TWO_DIM)

    irrigation_controller = Irrigation(main_pump_gpio=IrrigationGPIOs.MAIN_PUMP,
                                       water_sol_gpio=IrrigationGPIOs.WATER_SOL,
                                       tank_switch_sol_gpio=IrrigationGPIOs.TANK_SWITCH,
                                       nutr_sol_gpio=IrrigationGPIOs.NUTR_SOL,
                                       levels_sol_gpios=[gpio.value for gpio in LevelSolenoidsGPIOs],
                                       main_tank_empty_gpio=TankSensorGPIOs.MAIN_TANK_SENSOR_EMPTY,
                                       main_tank_full_gpio=TankSensorGPIOs.MAIN_TANK_SENSOR_FULL,
                                       drain_tank_empty_gpio=TankSensorGPIOs.DRAIN_TANK_SENSOR_EMPTY,
                                       drain_tank_full_gpio=TankSensorGPIOs.DRAIN_TANK_SENSOR_FULL)

    arm_controller = Arm(enable_gpio=ArmGPIOs.ENABLE, direction_gpio=ArmGPIOs.DIRECTION, pulse_gpio=ArmGPIOs.PULSE,
                         left_limit_sensor_gpio=ArmGPIOs.LEFT_LIMIT, right_limit_sensor_gpio=ArmGPIOs.RIGHT_LIMIT)
    air_controller = Air(AIR_MAIN_GPIO)

    def air_on(self):
        try:
            self.air_controller.on()
        except Exception as e:
            logging.error(e)

    def air_off(self):
        try:
            self.air_controller.on()
        except Exception as e:
            logging.error(e)

    def run_water_cycle(self):
        try:
            self.irrigation_controller.run_cycle()
        except Exception as e:
            logging.error(e)
            raise e

    # def sol_check(self):
    #     self.irrigation_controller.sol_check()
    #


actuator_controller = ActuatorController()