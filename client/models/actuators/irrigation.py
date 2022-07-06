from typing import List

from lighting import LedMain
import gpiozero
from gpiozero import DigitalOutputDevice
from gpiozero import DigitalInputDevice
import time
import logging

import os
import sys
# Modify PATH so we can import files from elsewhere in this repo
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '../..')))


class Irrigation:

    def __init__(self, main_pump_gpio, water_sol_gpio, tank_switch_sol_gpio, nutr_sol_gpio,
                 levels_sol_gpios: List,
                 main_tank_full_gpio, main_tank_empty_gpio, drain_tank_full_gpio, drain_tank_empty_gpio
                 ):
        self.main_pump = DigitalOutputDevice(main_pump_gpio)
        self.water_sol = DigitalOutputDevice(water_sol_gpio)
        self.tank_switch_sol = DigitalOutputDevice(tank_switch_sol_gpio)
        self.nutr_sol = DigitalOutputDevice(nutr_sol_gpio)
        self.levels_sols = [DigitalOutputDevice(level_sol_gpio) for level_sol_gpio in levels_sol_gpios]

        self.main_tank_full = DigitalInputDevice(main_tank_full_gpio, pull_up=True)
        self.main_tank_empty = DigitalInputDevice(main_tank_empty_gpio, pull_up=True)
        self.drain_tank_full = DigitalInputDevice(drain_tank_full_gpio, pull_up=True)
        self.drain_tank_empty = DigitalInputDevice(drain_tank_empty_gpio, pull_up=True)

    def run_cycle(self, duration=5, nutrient=False):
        ''' runs the water cycle for given time. at end of each irrigation
        process for level solenoid it checks for the water supply and verifies
        available water sources'''
        # Turning on the lvl sols
        # if(self.gotWater()):
        for sol in self.levels_sols:
            logging.INFO(sol, ' Turned on')
            sol.on()
            time.sleep(1)
            # Opening the water sol
            self.water_sol.on() if not nutrient else self.nutr_sol.on()
            time.sleep(1)
        # Opening the water sol
        self.water_sol.on() if not nutrient else self.nutr_sol.on()
        time.sleep(1)
        # Turning on the main pump
        self.main_pump.on()
        time.sleep(duration)
        # Turning off the main pump after the cycle time
        self.main_pump.off()
        time.sleep(1)
        # closing the water sol
        self.water_sol.on() if not nutrient else self.nutr_sol.on()
        # closing the lvl sols
        for sol in self.levels_sols:
            logging.INFO(sol, ' Turned off')
            sol.off()
            time.sleep(1)

    def has_water(self):
        if not self.main_tank_empty.is_active:  # Main Tank is not empty
            self.tank_switch_sol.power_off()  # make sure the tank switch relay is off
            return True
        elif self.main_tank_empty.is_active:
            # Case where main tank is empty
            if not self.drain_tank_empty.is_active:  # Case where the drain tank is not empty
                self.panic_mode()  # add the lesser panic drill
                LedMain.dim(0, 0, 0)
                # turn off fans
                # activate tank switch relay to switch from main tank to drain tank
                self.tank_switch_sol.on()
                return True
            elif self.drain_tank_empty.is_active:  # if the drain tank is empty too
                self.panic_mode()  # Add the panic drill
                LedMain.dim(0, 0, 0)  # turn off lights
                return False

    def panic_mode(self):
        ''' function for flashing all the lights'''
        for _ in range(30):
            LedMain.dim(1, 1, 1)
            time.sleep(1)
            LedMain.dim(0.5, 0.5, 0.5)
            time.sleep(1)
            LedMain.dim(0, 0, 0)
            time.sleep(1)

    def tank_full(self):
        ''' function that checks when any of the water tanks get full and runs the panic drill
        if they are full'''
        if self.main_tank_full.is_active or self.drain_tank_full.is_active:
            self.panic_mode()


''' Add a indicator on dashoboard tanks levels are full or empty. '''

# Main pump only can be on if water sol is on and lvl one sol is on
