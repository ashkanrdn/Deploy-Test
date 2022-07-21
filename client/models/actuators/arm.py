import gpiozero
import time
from time import sleep
import logging
from enum import Enum
from datetime import datetime


class Direction(Enum):
    Right = 0
    Left = 1


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
        self.day_swing_duration = 12

    def calibrate(self):
        """calibration routine to set the zero position and max step position.
        Note: zero postion gets callibrated everytime left proximity is triggered."""
        self.go_to_start_location(direction=Direction.Right)
        # LEDMAIN(Alert)
        self.total_steps = 0
        self.lock = 0
        sleep(1)

        logging.info('Far Right Reached')
        while not self.has_reached_limit(Direction.Left):
            self.pulsate(direction=Direction.Left)
            self.total_steps += 1
            self.lock += 1

    def go_to_start_location(self, direction):
        while not self.has_reached_limit(direction):
            self.pulsate(direction)

    def get_pin_direction(self):
        return Direction.Right if self.direction.is_active else Direction.Right

    def set_pin_direction(self, direction: Direction):
        self.direction.on() if direction is Direction.Right else self.direction.off()

    def has_reached_limit(self, direction: Direction):
        if direction is Direction.Left:
            return self.left_limit_sensor.is_active
        else:
            return self.right_limit_sensor.is_active

    def pulsate(self, direction: Direction):
        """to move the stepper one step in a direction assigned every time it is called"""
        # self.ARMEna.on()

        if not self.has_reached_limit(direction=direction):  # Check if ARM has reached far left #TODO

            if self.get_pin_direction() is not direction:  # check the status of direction pin and set it accordingly
                sleep(0.25)
                self.set_pin_direction(direction)
                sleep(0.25)
                # set pulse pin on and off
            sleep(Arm.sleep_duration)
            self.pulse.off()
            sleep(Arm.sleep_duration)
            self.pulse.on()
            self.lock += 1 if direction is Direction.Right else -1
            logging.info(f'Moved to Direction {direction.name}')
        else:
            logging.warning(f'Reached the limit on {direction.name}')

    def go_to_location_by_hour(self, hour, speed=100):
        """

        :param hour: an hour between 1 to day_swing_duration
        :param speed:
        :return: None
        """
        location = (self.day_swing_duration - hour) * self.total_steps / self.day_swing_duration
        # actual_steps = int((location * self.total_steps) / 100) if location else 0

        pause = 1
        if location > self.lock:
            while self.lock > location:
                self.pulsate(direction=Direction.Left)
        elif location < self.lock:
            while self.lock < location:
                self.pulsate(direction=Direction.Right)

    def day_swing_pulsate(self, interval_duration, day_window):
        current_time = datetime.now()
        if not day_window[0] < current_time.time() < day_window[1]:
            return
        interval_steps = self.total_steps * interval_duration / (12 * 3600)
        steps = 0

        while steps < interval_steps:
            if self.has_reached_limit(Direction.Left):
                logging.warning('Reached the left soon!')
                return
            self.pulsate(Direction.Left)

    # def to_home(self):
    #     self.go_to_loc(0)
