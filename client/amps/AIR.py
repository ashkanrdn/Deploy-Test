import gpiozero
from gpiozero import DigitalOutputDevice
import time

class AIR():
    def __init__(self,gpioAIRMain):
        self.AIRMain =DigitalOutputDevice(gpioAIRMain)

    def On(self):
        self.AIRMain.on()
        print('On')

    def Off(self):
        self.AIRMain.off()
        print('off')
