import gpiozero
from gpiozero import DigitalOutputDevice
import time


class Fan:
    def __init__(self, fan_gpio):
        self.fan = DigitalOutputDevice(fan_gpio)

    def on(self):
        self.fan.on()

    def off(self):
        self.fan.off()
