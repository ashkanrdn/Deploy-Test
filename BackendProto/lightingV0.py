import gpiozero
from gpiozero import DigitalOutputDevice
from gpiozero import PWMLED
import time



hello=5555555555554444
#Lighting Control Basic Function

ledMainPwr = DigitalOutputDevice(18)
#need to add comments


class LedMain(PWMLED):
    
    def __init__(self, guid):
        super().__init__(guid)
    def dim(self,level):
        if ledMainPwr.is_active == False:
            ledMainPwr.on()
        self.Dim(level)
    def source(self,source):
        if ledMainPwr.is_active == False:
            ledMainPwr.on()
        self.source(source)
    def off(self):
        ledMainPwr.off()
   
ledGrow = LedMain(25)
ledSuppOne = PWMLED(10)
ledSuppTwo = PWMLED(24)



