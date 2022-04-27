# from amps.LED import LedMain
import gpiozero
from gpiozero import DigitalOutputDevice
from gpiozero import DigitalInputDevice
import time
import datetime

import os
import sys
# Modify PATH, so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))


class Irrigation():

    def __init__(self, main_pump_gpio, lvl1_sol_gpio):
        self.IRGMainPump = DigitalOutputDevice(main_pump_gpio)
        self.IRGlvl1Sol = DigitalOutputDevice(lvl1_sol_gpio)
        self.sol_status = False
        self.sol_on_time = datetime.datetime.now()

    def run_water_cycle(self, duration=5):
        ''' runs the water cycle for given time. at end of each irrigation
        process for level solenoid it checks for the water supply and verifies
        available water sources'''
        self.IRGlvl1Sol.on()
        self.sol_on_time = datetime.datetime.now()
        self.sol_status = True
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
        self.sol_status = False
        time.sleep(1)

    def sol_check(self):
        time_delta = datetime.datetime.now() - self.sol_on_time
        if self.sol_status and time_delta >= datetime.timedelta(seconds=60):
            self.IRGlvl1Sol.off()
            self.sol_status = False

''' Add a indicator on dashboard tanks levels are full or empty. '''

# Main pump only can be on if water sol is on and lvl one sol is on
