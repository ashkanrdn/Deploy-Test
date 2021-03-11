import gpiozero
from gpiozero import DigitalOutputDevice
import time


#   IRGMainPump, IRGWtrPump, IRGTrnsPump, IRGNutrPump ,
            # IRGlvl1Sol, IRGlvl2Sol, IRGlvl3Sol, IRGlvl4Sol, IRGlvl5Sol



class Irrigation():
    def __init__(self,gpioMainPump, gpioWtrPump,gpioTrnsPump, gpioNutrPump,
            gpiolvl1Sol, gpiolvl2Sol, gpiolvl3Sol, gpiolvl4Sol, gpiolvl5Sol,
            IRGMainPump, IRGWtrPump, IRGTrnsPump, IRGNutrPump ,
            IRGlvl1Sol, IRGlvl2Sol, IRGlvl3Sol, IRGlvl4Sol, IRGlvl5Sol): #add level sensor GOPIO and level Sensor Input



        self.IRGMainPump = DigitalOutputDevice(gpioMainPump)
        self.IRGWtrPump = DigitalOutputDevice(gpioWtrPump)
        self.IRGTrnsPump = DigitalOutputDevice(gpioTrnsPump)
        self.IRGNutrPump = DigitalOutputDevice(gpioNutrPump)
        self.IRGlvl1Sol = DigitalOutputDevice(gpiolvl1Sol)
        self.IRGlvl2Sol = DigitalOutputDevice(gpiolvl2Sol)
        self.IRGlvl3Sol = DigitalOutputDevice(gpiolvl3Sol)
        self.IRGlvl4Sol = DigitalOutputDevice(gpiolvl4Sol)
        self.IRGlvl5Sol = DigitalOutputDevice(gpiolvl5Sol)
        self.IRGPumps = [self.IRGMainPump,self.IRGWtrPump,self.IRGTrnsPump,self.IRGNutrPump]

    def waterCycle(self,IRGPumps, cycleTime):
        self.IRGMainPump.on()
        time.sleep(1)
        self.IRGNutrPump()
        time.sleep(1)
        for i in range(len(self.IRGPumps)):
            print(i)

            # pump.on()
            # time.sleep(cycleTime)


