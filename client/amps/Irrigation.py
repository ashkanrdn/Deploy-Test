import gpiozero
from gpiozero import DigitalOutputDevice
import time






class Irrigation():
    def __init__(self,gpioMainPump, gpioWtrPump,gpioTrnsPump, gpioNutrPump,
                gpiolvl1Sol, gpiolvl2Sol, gpiolvl3Sol, gpiolvl4Sol, gpiolvl5Sol): #add level sensor GOPIO and level Sensor Input



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

    def waterCycle(self, cycleTime):
        # self.IRGMainPump.on()
        # time.sleep(1)
        # self.IRGNutrPump()
        # time.sleep(1)
        for i in self.IRGPumps:

            print(i)
            self.IRGMainPump.on()
            self.IRGWtrPump.on()
            self.IRGTrnsPump.on()
            self.IRGNutrPump.on()
            self.IRGlvl1Sol.on()
            self.IRGlvl2Sol.on()
            self.IRGlvl3Sol.on()
            self.IRGlvl4Sol.on()
            self.IRGlvl5Sol.on()
            time.sleep(2)

            # pump.on()
            # time.sleep(cycleTime)



Wtring =Irrigation(gpioMainPump=14, gpioWtrPump=15,gpioTrnsPump=18, gpioNutrPump=23,
                gpiolvl1Sol=24, gpiolvl2Sol=25, gpiolvl3Sol=8, gpiolvl4Sol=7, gpiolvl5Sol=1)

Wtring.waterCycle(0.1)
