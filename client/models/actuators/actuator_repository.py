from .config import *
from .lighting import Led
from .fan import Fan
from .irrigation import Irrigation
import logging
logging.basicConfig(filename='amps_actuator.log',
    format='%(asctime)s %(levelname)s: %(message)s',
 level=logging.INFO)


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


    def fans_on(self):
        try:
            [fan.on() for fan in self.fans]
        except Exception as e:
            logging.error(e)


    def fans_off(self):
        try:
            [fan.off() for fan in self.fans]
        except Exception as e:
            logging.error(e)


    def lights_on(self):
        try:
            self.main_led.on() 
        except Exception as e:
            logging.error(e)


    def lights_off(self):
        try:
            self.main_led.off() 
        except Exception as e:
            logging.error(e)

    def run_water_cycle(self):
        try:
            self.irrigation.run_water_cycle() 
        except Exception as e:
            logging.error(e)
            raise e       

    def sol_check(self):
        self.irrigation.sol_check()

actuator_repository = ActuatorRepository()
