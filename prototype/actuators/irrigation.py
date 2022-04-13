# from amps.LED import LedMain
import gpiozero
from gpiozero import DigitalOutputDevice
from gpiozero import DigitalInputDevice
import time

import os
import sys
# Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))


class Irrigation():

    def __init__(self, gpioIRGMainPump, gpioIRGlvl1Sol):
        self.IRGMainPump = DigitalOutputDevice(gpioIRGMainPump)
        self.IRGlvl1Sol = DigitalOutputDevice(gpioIRGlvl1Sol)
        self.IRGlvlSols = [self.IRGlvl1Sol]

    def waterCycle(self, cycleTime=5):
        ''' runs the water cycle for given time. at end of each irrigation
        process for level solenoid it checks for the water supply and verifies
        available water sources'''
        # Turning on the lvl sols
        # if(self.gotWater()):
        for lvlSol in self.IRGlvlSols:
            lvlSol.on()
            time.sleep(1)
            time.sleep(1)

        # Turning on the main pump
        self.IRGMainPump.on()
        time.sleep(cycleTime)
        # Turning off the main pump after the cycle time
        self.IRGMainPump.off()
        time.sleep(1)

        # closing the lvl sols
        for lvlSol in self.IRGlvlSols:
            lvlSol.off()
            time.sleep(1)

    # def panicMode(self): 
    #     ''' function for flashing all the lights'''
    #     for _ in range(30):
    #         LedMain.dim(1, 1, 1)
    #         time.sleep(1)
    #         LedMain.dim(0.5, 0.5, 0.5)
    #         time.sleep(1)
    #         LedMain.dim(0, 0, 0)
    #         time.sleep(1)

''' Add a indicator on dashoboard tanks levels are full or empty. '''

# Main pump only can be on if water sol is on and lvl one sol is on
