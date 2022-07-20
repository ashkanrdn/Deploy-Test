import gpiozero
import time
from time import sleep
import logging


class LedMain():
    ''' The LedMain class controls the main LED grow light:
        gpioPwr is the raspberry pi pin assignment for Main LED Power on/off
        gpioDim is the raspberry pi pin assignment for Main LED Dim controller
        gpioSupp1 is the raspberry pi pin assignment for Supplemental 1 controller
        gpioSupp2 is the raspberry pi pin assignment for Supplemental 2 controller

        on: turns all on
        dim: controls the dim level of the MainLED
            level: the level of dim for MainLED 0 min. 1 max.
            all supplemental LEDs arelevels are assigned as percentage of main
        off: turns all off'''

    def __init__(self, power_gpio, dim_gpio, supp1_gpio, supp2_gpio, supp1_dim=0.5, supp2_dim=0.5, main_dim=0.5):
        # assign MainLED power on/off
        self.main_led_power = gpiozero.DigitalOutputDevice(power_gpio)
        # assign lightingLedMain
        self.main_led = gpiozero.PWMLED(
            dim_gpio)
        # assign lightingLedSuppOne as PWMLED
        self.led_supp_one = gpiozero.PWMLED(supp1_gpio)
        # assign lightingLedSuppTwo as PWMLED
        self.led_supp_two = gpiozero.PWMLED(supp2_gpio)
        # setting the initial Dim value for lightingLedSuppOne
        self.led_supp_one_dim = supp1_dim
        # setting the initial Dim value for lightingLedSuppTwo
        self.led_supp_two_dim = supp2_dim
        logging.info('Class Initiated')

    def power_on(self):
        '''Powers on the main PWR, main LED and supplemental LED's at last set levels'''
        self.main_led_power.power_on()
        time.sleep(.5)
        self.main_led.power_on()
        self.led_supp_one.power_on()
        self.led_supp_two.power_on()

    def dim(self, main_dim=0, supp1_dim=0, supp2_dim=0):
        """Set the dim level for the main LED. The supplemental LED's are asigned based on the configuration file data
         as a percentage of the MainLED level"""
        if not self.main_led_power.is_active:
            self.main_led_power.power_on()

        self.main_led.value = main_dim
        self.led_supp_one.value = supp1_dim
        self.led_supp_two.value = supp2_dim

    def power_off(self):
        """Powers off the main PWR, main LED and supplemental LED's at last set levels"""
        self.main_led.power_off()
        self.led_supp_one.power_off()
        self.led_supp_two.power_off()

        self.main_led_power.power_off()

    def calibrate(self, supp_one_level, supp_two_level):
        # figure out how to calibrate supp LEDs
        self.main_led_power.power.power_on()

        # set supplemental one level:
        self.led_supp_one.value = supp_one_level
        self.led_supp_two.value = supp_two_level
        self.led_supp_one_percentage = (self.led_supp_one.value / self.main_led)
        self.led_supp_two_percentage = (self.led_supp_two.value / self.main_led)

    def panic_mode(self):
        ''' function for flashing all the lights'''
        for _ in range(30):
            self.dim(1, 1, 1)
            time.sleep(1)
            self.dim(0.5, 0.5, 0.5)
            time.sleep(1)
            self.dim(0, 0, 0)
            time.sleep(1)
