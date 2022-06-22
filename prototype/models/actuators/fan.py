import gpiozero
from gpiozero import DigitalOutputDevice
import time


class Fan:
    def __init__(self, fan_gpio):
        self.status = False
        self.fan = DigitalOutputDevice(fan_gpio)

    def on(self):
        if not self.status:
            self.fan.on()
            self.status = True
            print('Fan Turned On')

    def off(self):
        if self.status:
            self.fan.off()
            self.status = False
            print('Fan Turned Off')

