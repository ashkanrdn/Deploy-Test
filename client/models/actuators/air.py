import gpiozero
from gpiozero import DigitalOutputDevice
import time
import logging


# TODO add timing to the logging info

class Air:
    def __init__(self, main_air_gpio):
        self.AIRMain = DigitalOutputDevice(main_air_gpio)
        
    def status(self):
        return 1

    def on(self):
        self.AIRMain.off()
        logging.info('air on')

    def off(self):
        self.AIRMain.on()
        logging.info('air off')
