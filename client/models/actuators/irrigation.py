from typing import List

# from .lighting import LedMain
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

    def __init__(self, water_sol_gpio, tank_switch_sol_gpio, nutr_sol_gpio,
                 levels_sol_gpios: List,
                 pressure_relief_gpio
                 ):
        self.water_sol = DigitalOutputDevice(water_sol_gpio)
        self.pressure_relief_sol = DigitalOutputDevice(pressure_relief_gpio)
        self.tank_switch_sol = DigitalOutputDevice(tank_switch_sol_gpio)
        self.nutr_sol = DigitalOutputDevice(nutr_sol_gpio)
        self.levels_sols = [DigitalOutputDevice(level_sol_gpio) for level_sol_gpio in levels_sol_gpios]


    

    # def run_cycle(self, duration, nutrient=False, levels=None):

    #     source_sol = self.nutr_sol if nutrient else self.water_sol
    #     water_sleep_time = 1
    #     pressure_relief_time = 2
    #     source_sol.on()
    #     print(source_sol, 'Source Solenoid Turned On!')
    #     print(f'Waiting for {water_sleep_time} seconds...')
    #     time.sleep(water_sleep_time)

    #     #Pressure Relief Turn On
    #     self.pressure_relief_sol.on()
    #     print(self.pressure_relief_sol, 'Pressure Relief Solenoid Turned On!')
    #     print(f'Waiting for {pressure_relief_time} seconds...')
    #     time.sleep(pressure_relief_time)
    #     self.pressure_relief_sol.off()
    #     print(self.pressure_relief_sol, 'Pressure Relief Solenoid Turned Off!')


    #     #Levels
    #     levels_sols = [self.levels_sols[level] for level in levels] if levels else self.levels_sols
    #     level_pressure_time = 5
    #     for sol in levels_sols:
    #         sol.on()
    #         print(sol, 'Solenoid level Turned On!')
    #         print(f'Waiting for {level_pressure_time} seconds...')
    #         time.sleep(level_pressure_time)
    #         sol.off()
    #         print(sol, 'Solenoid level Turned Off!')
    #         self.pressure_relief_sol.on()
    #         print(self.pressure_relief_sol, 'Pressure Relief Solenoid Turned On!')
    #         print(f'Waiting for {duration} seconds...')
    #         time.sleep(duration)
    #         self.pressure_relief_sol.off()
    #         print(self.pressure_relief_sol, 'Pressure Relief Solenoid Turned Off!')
    #         time.sleep(1)
    #         print('Irrigation for this level has been completed!')

    #     source_sol.off()
    #     print(source_sol, 'Source Solenoid Turned On!') 
        

    def run_cycle(self, duration, nutrient=False, levels=None):
        source_sol = self.nutr_sol if nutrient else self.water_sol
        levels_sols = [self.levels_sols[level-1] for level in levels] if levels else self.levels_sols
        print(levels, levels_sols)
        # return
        primeTime = 40
        source_sol.on()
        time.sleep(20)
        # #levels
        for i,sol in enumerate(levels_sols):
            self.run_cycle_level(levels[i], duration)

        source_sol.off()

    def run_cycle_level(self, level, duration):
        sol = self.levels_sols[level - 1]
        primeTime = 40
        print(f'Prime Process running for level {level}')
        self.pressure_relief_sol.on()
        print('Pressure relief sol is on!')
        sol.on()
        print(f'Solenoid level {level} is on!')
        print(f'Sleeping for {primeTime}...')

        time.sleep(primeTime)
        self.pressure_relief_sol.off()
        print('Pressure relief sol is off!')

        print(f'Sleeping for {duration}...')

        time.sleep(duration)
        sol.off()
        print(f'Solenoid level {level} is off!')

        print(f'draingin level {level}!')

        time.sleep(1)
        self.pressure_relief_sol.on()
        print('Pressure relief sol is on!')

        time.sleep(20)
        self.pressure_relief_sol.off()
        print('Pressure relief sol is off!')

        time.sleep(1)



    def sol_check(self):
        for sol in self.levels_sols:
            sol.off()
            print(sol, 'off')
            time.sleep(1)
        self.water_sol.off()
        print('water_sol_off')
