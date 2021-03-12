import gpiozero
from gpiozero import DigitalOutputDevice
import time


#   IRGMainPump, IRGWtrSol, IRGTrnsPump, IRGNutrSol ,
            # IRGlvl1Sol, IRGlvl2Sol, IRGlvl3Sol, IRGlvl4Sol, IRGlvl5Sol



class Irrigation():
    def __init__(self,gpioMainPump, gpioWtrSol,gpioTrnsPump, gpioNutrSol,
                gpiolvl1Sol, gpiolvl2Sol, gpiolvl3Sol, gpiolvl4Sol, gpiolvl5Sol,
                ): #add level sensor GOPIO and level Sensor Input



        self.IRGMainPump = DigitalOutputDevice(gpioMainPump)
        self.IRGWtrSol = DigitalOutputDevice(gpioWtrSol)
        self.IRGTrnsPump = DigitalOutputDevice(gpioTrnsPump)
        self.IRGNutrSol = DigitalOutputDevice(gpioNutrSol)
        self.IRGlvl1Sol = DigitalOutputDevice(gpiolvl1Sol)
        self.IRGlvl2Sol = DigitalOutputDevice(gpiolvl2Sol)
        self.IRGlvl3Sol = DigitalOutputDevice(gpiolvl3Sol)
        self.IRGlvl4Sol = DigitalOutputDevice(gpiolvl4Sol)
        self.IRGlvl5Sol = DigitalOutputDevice(gpiolvl5Sol)
        self.IRGlvlSols = [self.IRGlvl1Sol, self.IRGlvl2Sol,self.IRGlvl3Sol,self.IRGlvl4Sol,self.IRGlvl5Sol]

    def waterCycle(self, cycleTime):
        self.IRGMainPump.on()
        time.sleep(1)
        self.IRGWtrSol.on()
        time.sleep(1)
        for lvlSol in self.IRGlvlSols:
            # check supply tank level and transfer routine
            print(lvlSol)
            lvlSol.on()
            time.sleep(cycleTime)
            lvlSol.off()
        time.sleep(1)
        self.IRGWtrSol.off()
        time.sleep(1)
        self.IRGMainPump.off()

    def nutrientCycle(self,cycleTime):
        self.IRGMainPump.on()
        time.sleep(1)
        self.IRGNutrSol.on()
        time.sleep(1)
        for lvlSol in self.IRGlvlSols:
            # check supply tank level and transfer routine
            lvlSol.on()
            time.sleep(cycleTime)
            lvlSol.off()
        time.sleep(1)
        self.IRGNutrSol.off()
        time.sleep(1)
        self.IRGMainPump.off()

# define transfer routine




