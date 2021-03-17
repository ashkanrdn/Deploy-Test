import gpiozero
from gpiozero import DigitalOutputDevice
from gpiozero import DigitalInputDevice
import time

import os
import sys
 # Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from amps.lightingClass import LedMain


#   IRGMainPump, IRGWtrSol, IRGTankSwitchSol, IRGNutrSol ,
            # IRGlvl1Sol, IRGlvl2Sol, IRGlvl3Sol, IRGlvl4Sol, IRGlvl5Sol



class Irrigation():
    def __init__(self,gpioIRGMainPump, gpioIRGWtrSol,gpioIRGTankSwitchSol, gpioIRGNutrSol,
                gpioIRGlvl1Sol, gpioIRGlvl2Sol, gpioIRGlvl3Sol, gpioIRGlvl4Sol, gpioIRGlvl5Sol
                ): #add level sensor GOPIO and level Sensor Input
                # ,gpioIRGIRGMainTankSensor,gpioIRGIRGDrainTankSensor


        self.IRGMainPump = DigitalOutputDevice(gpioIRGMainPump)
        self.IRGWtrSol = DigitalOutputDevice(gpioIRGWtrSol)
        self.IRGTankSwitchSol = DigitalOutputDevice(gpioIRGTankSwitchSol)
        self.IRGNutrSol = DigitalOutputDevice(gpioIRGNutrSol)
        self.IRGlvl1Sol = DigitalOutputDevice(gpioIRGlvl1Sol)
        self.IRGlvl2Sol = DigitalOutputDevice(gpioIRGlvl2Sol)
        self.IRGlvl3Sol = DigitalOutputDevice(gpioIRGlvl3Sol)
        self.IRGlvl4Sol = DigitalOutputDevice(gpioIRGlvl4Sol)
        self.IRGlvl5Sol = DigitalOutputDevice(gpioIRGlvl5Sol)
        self.IRGlvlSols = [self.IRGlvl1Sol, self.IRGlvl2Sol,self.IRGlvl3Sol,self.IRGlvl4Sol,self.IRGlvl5Sol]
        # self.IRGMainTankSensor = DigitalInputDevice(gpioIRGMainTankSensor)
        # self.IRGDrainTankSensor = DigitalInputDevice(gpioIRGDrainTankSensor)

    def waterCycle(self, cycleTime=5):
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

    def nutrientCycle(self,cycleTime =5):
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

    # def tankFull(self):
    '''Function to check Main tanks sensor
     and flash the lights when it full'''
    #     if(self.IRGMainTankSensor == True):
    #         for i in range(30):
    #             LedMain.dim(1,1,1)
    #             time.sleep(0.1)
    #             LedMain.dim(0,0,0)
    #             time.sleep(0.1)


    # def tanksEmpty(self):
    '''Function to check Main tanks and the drain tank sensor
    and flash the lights when it empty'''

    #     if((self.IRGMainTankSensor == False) and (self.IRGDrainTankSensor==False)):
    #         for i in range(30):
    #             LedMain.dim(1,1,1)
    #             time.sleep(1)
    #             LedMain.dim(0.5,0.5,0.5)
    #             time.sleep(1)
    #             LedMain.dim(0,0,0)
    #             time.sleep(1)




    # def gotWater(self):
    #     if(self.IRGMainTankSensor):
    #         self.IRGWtrSol.on()
    #         self.
    #     elif (self.IRGMainTankSensor ==False and self.IRGDrainTankSensor == True):



# define transfer routine




