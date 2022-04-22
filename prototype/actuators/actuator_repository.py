from .config import *
from .lighting import Led
from .fan import Fan
from .irrigation import Irrigation


class ActuatorRepository:
    def __init__(self):
        self.main_led = Led(dim_gpio=LightGPIOs.MAIN_LED.value)
        print('led instantiated')
        self.fans = [
            Fan(fan_gpio=FanGPIOs.FAN_ONE.value),
            Fan(fan_gpio=FanGPIOs.FAN_TWO.value),
            Fan(fan_gpio=FanGPIOs.FAN_THREE.value)
        ]
        print('fans instantiated')

        self.irrigation = Irrigation(main_pump_gpio=IrrigationGPIOs.MAIN_PUMP.value,
                                     lvl1_sol_gpio=IrrigationGPIOs.LEVEL_ONE_SOL.value)
        print('irrigation instantiated')
