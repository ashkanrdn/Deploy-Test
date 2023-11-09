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

    def __init__(self, power_gpio, 
    # dim_gpio, 
    # supp1_gpio, 
    # supp2_gpio, 
    # supp1_dim=0.5, 
    # supp2_dim=0.5, 
    # main_dim=0.5
    ):
        # assign MainLED power on/off
        self.main_led_power = gpiozero.DigitalOutputDevice(power_gpio)
        # assign lightingLedMain
        # self.main_led = gpiozero.PWMLED(
        #     dim_gpio)
        # self.main_led.frequency = 1000

        # # assign lightingLedSuppOne as PWMLED
        # self.led_supp_one = gpiozero.PWMLED(supp1_gpio)
        # self.led_supp_one.frequency = 1000

        # # assign lightingLedSuppTwo as PWMLED
        # self.led_supp_two = gpiozero.PWMLED(supp2_gpio)
        # self.led_supp_two.frequency = 1000

        # # setting the initial Dim value for lightingLedSuppOne
        # self.led_supp_one_dim = supp1_dim
        # # setting the initial Dim value for lightingLedSuppTwo
        # self.led_supp_two_dim = supp2_dim
        logging.info('Class Initiated')

    def power_on(self):
        '''Powers on the main PWR, main LED and supplemental LED's at last set levels'''
        self.main_led_power.on()
        # time.sleep(.5)
        # self.main_led.off() #works reversly
        # self.led_supp_one.on()
        # self.led_supp_two.on()

    def dim(self, main_dim=0, supp1_dim=0, supp2_dim=0): #keep main dim at 0
        """Set the dim level for the main LED. The supplemental LED's are asigned based on the configuration file data
         as a percentage of the MainLED level"""
        raise NotImplementedError

    def power_off(self):
        """Powers off the main PWR, main LED and supplemental LED's at last set levels"""
        self.main_led_power.off()



    def calibrate(self, supp_one_level, supp_two_level):
        raise NotImplementedError

    def panic_mode(self):
        ''' function for flashing all the lights'''
        pass
        
    def status(self):
        return self.main_led_power.value