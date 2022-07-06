import gpiozero
from gpiozero import DigitalOutputDevice
import time
import logging


class Air:
    def __init__(self, main_air_gpio):
        self.AIRMain = DigitalOutputDevice(main_air_gpio)

    def on(self):
        self.AIRMain.on()
        print('On')

    def off(self):
        self.AIRMain.off()
        print('off')
