import gpiozero
import time
from time import sleep
import logging


class Arm:

    sleep_duration = 0.0000025  # internal sleep variable

    def __init__(self, enable_gpio, direction_gpio, pulse_gpio, left_limit_sensor_gpio, right_limit_sensor_gpio,
                 lock=0, total_steps=100000, revolution=400):
        self.ARMPins = [enable_gpio, direction_gpio, pulse_gpio]
        self.enable = gpiozero.OutputDevice(enable_gpio)
        self.direction = gpiozero.OutputDevice(direction_gpio)
        self.pulse = gpiozero.OutputDevice(pulse_gpio)
        self.left_limit_sensor = gpiozero.InputDevice(left_limit_sensor_gpio, pull_up=True)
        self.right_limit_sensor = gpiozero.InputDevice(right_limit_sensor_gpio, pull_up=True)
        self.lock = lock
        self.total_steps = total_steps
        self.revolution = revolution

    def calibrate(self):
        """calibration routine to set the zero position and max step position.
        Note: zero postion gets callibrated everytime left proximity is triggered."""
        while not self.left_limit_sensor.is_active:
            self.pulsate(direction='L')
        # LEDMAIN(Alert)
        self.total_steps = 0
        self.lock = 0
        sleep(1)

        logging.info('Far Left Reached')
        while not self.right_limit_sensor.is_active:
            self.pulsate(direction='R')
            self.total_steps += 1
            self.lock += 1
        # LEDMAIN(Alert)

        # moveTo(pos=0)
        # LEDMAIN(Homage)

    def pulsate(self, direction):
        """to move the stepper one step in a direction assigned every time it is called"""
        # self.ARMEna.on()
        if direction == 'L':
            if not self.left_limit_sensor.is_active:  # Check if ARM has reached far left

                if not self.direction.is_active:  # check the status of direction pin and set it accordingly
                    sleep(0.25)
                    self.direction.on()
                    sleep(0.25)
                    # set pulse pin on and off
                sleep(Arm.sleep_duration)
                self.pulse.off()
                sleep(Arm.sleep_duration)
                self.pulse.on()
                self.lock -= 1
        elif direction == 'R':

            if not self.right_limit_sensor.is_active:
                if self.direction.is_active:
                    sleep(Arm.sleep_duration)
                    self.direction.off()
                    sleep(Arm.sleep_duration)

                sleep(Arm.sleep_duration)
                self.pulse.off()
                sleep(Arm.sleep_duration)
                self.pulse.on()
                self.lock += 1

        else:
            logging.info('Direction ')

    def go_to_loc(self, location, speed=100):

        actual_steps = int((location * self.total_steps) / 100) if location else 0

        pause = 1

        if actual_steps > self.lock:
            while actual_steps >= self.lock:
                self.pulsate(direction='R')

        elif actual_steps < self.lock:
            while actual_steps <= self.lock:
                self.pulsate(direction='L')

    def to_home(self):
        self.go_to_loc(0)
