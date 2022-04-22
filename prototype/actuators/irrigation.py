# from amps.LED import LedMain
import gpiozero
from gpiozero import DigitalOutputDevice
from gpiozero import DigitalInputDevice
import time

import os
import sys
# Modify PATH, so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))


class Irrigation():

    def __init__(self, main_pump_gpio, lvl1_sol_gpio):
        self.IRGMainPump = DigitalOutputDevice(main_pump_gpio)
        self.IRGlvl1Sol = DigitalOutputDevice(lvl1_sol_gpio)

    def run_water_cycle(self, duration=5):
        ''' runs the water cycle for given time. at end of each irrigation
        process for level solenoid it checks for the water supply and verifies
        available water sources'''
        self.IRGlvl1Sol.on()
        print('sol on')
        time.sleep(1)
        time.sleep(1)

        # Turning on the main pump
        self.IRGMainPump.on()
        print('pump on')

        time.sleep(duration)
        # Turning off the main pump after the cycle time
        self.IRGMainPump.off()
        print('pump off')
        time.sleep(1)

        # closing the lvl sols
        self.IRGlvl1Sol.off()
        print('sol off')
        time.sleep(1)


''' Add a indicator on dashboard tanks levels are full or empty. '''

# Main pump only can be on if water sol is on and lvl one sol is on
