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
                gpioIRGlvl1Sol, gpioIRGlvl2Sol, gpioIRGlvl3Sol, gpioIRGlvl4Sol, gpioIRGlvl5Sol,
                gpioIRGMainTankSensorFull,gpioIRGMainTankSensorEmpty,gpioIRGDrainTankSensorFull,gpioIRGDrainTankSensorEmpty
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
        self.IRGMainTankSensorFull = DigitalInputDevice(gpioIRGMainTankSensorFull,pull_up= True)
        self.IRGMainTankSensorEmpty = DigitalInputDevice(gpioIRGMainTankSensorEmpty,pull_up= True)
        self.IRGDrainTankSensorFull = DigitalInputDevice(gpioIRGDrainTankSensorFull,pull_up= True)
        self.IRGDrainTankSensorEmpty = DigitalInputDevice(gpioIRGDrainTankSensorEmpty,pull_up= True)

    def waterCycle(self, cycleTime=5):
            ''' runs the water cycle for given time. at end of each irrigation
            process for level solenoid it checks for the water supply and verifies
            available water sources'''
        self.IRGMainPump.on()
        time.sleep(1)
        self.IRGWtrSol.on()
        time.sleep(1)
        for lvlSol in self.IRGlvlSols:
            if(self.gotWater()):# check supply tank level and transfer routine
                print(lvlSol)
                lvlSol.on()
                time.sleep(cycleTime)
                lvlSol.off()
            else:
                break
        time.sleep(1)
        self.IRGWtrSol.off()
        time.sleep(1)
        self.IRGMainPump.off()

    def nutrientCycle(self,cycleTime =5):
            ''' runs the nutrient cycle for given time.  at end of each irrigation
            process for level solenoid it checks for the water supply and verifies
            available water sources'''
        self.IRGMainPump.on()
        time.sleep(1)
        self.IRGNutrSol.on()
        time.sleep(1)
        for lvlSol in self.IRGlvlSols:
            if(self.gotWater()):
            # check supply tank level and transfer routine
                lvlSol.on()
                time.sleep(cycleTime)
                lvlSol.off()
            else:
                break
        time.sleep(1)
        self.IRGNutrSol.off()
        time.sleep(1)
        self.IRGMainPump.off()

    def gotWater(self):
            ''' check the floating sensors and verifies water is available in supply tanks
            and operates the tank switch accordingly if it supplies water from drain tank
            it runs the panic drill to notify operator to fill the main tank if there is no water
            avaiable it breakes the irrigation cycle level loop '''
        if self.IRGMainTankSensorEmpty.is_active == False: #Main Tank is not empty
            self.IRGTankSwitchSol.off() #make sure the tank switch relay is off
            return True
        elif self.IRGMainTankSensorEmpty.is_active == True: #Case where main tank is empty
            if self.IRGDrainTankSensorEmpty.is_active == False: #Case where the drain tank is not empty
                self.panicMode()# add the lesser panic drill
                LedMain.dim(0,0,0)

                #turn off fans
                self.IRGTankSwitchSol.on() #activate tank switch relay to switch from main tank to drain tank
                return True
            elif self.IRGDrainTankSensorEmpty.is_active == True : #if the drain tank is empty too
                self.panicMode() #Add the panic drill
                LedMain.dim(0,0,0) # turn off lights
                return False





    def panicMode(self):
        ''' function for flashing all the lights'''
        for _ in range(30):
            LedMain.dim(1,1,1)
            time.sleep(1)
            LedMain.dim(0.5,0.5,0.5)
            time.sleep(1)
            LedMain.dim(0,0,0)
            time.sleep(1)

    def tankFull(self):
        ''' function that checks when any of the water tanks get full and runs the panic drill
        if they are full'''

        if (self.IRGMainTankSensorFull.is_active == True or self.IRGDrainTankSensorFull.is_active == True ):

            self.panicMode()








