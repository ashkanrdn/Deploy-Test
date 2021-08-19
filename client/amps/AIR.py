import gpiozero
from gpiozero import DigitalOutputDevice
import time
import logging


class AIR():
    def __init__(self, gpioAIRMain):
        self.AIRMain = DigitalOutputDevice(gpioAIRMain)

    def On(self):
        self.AIRMain.on()
        logging.INFO('On')

    def Off(self):
        self.AIRMain.off()
        logging.INFO('off')
