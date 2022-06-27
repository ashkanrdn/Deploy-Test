from pyexpat import native_encoding
import gpiozero
from gpiozero.pins.native import NativeFactory
from gpiozero import Device, LED, PWMLED
import time
from time import sleep

native_factory = NativeFactory()
class Led():
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

    status = False

    def __init__(self, dim_gpio, dim_value=1):

        self.main_lighting_led = gpiozero.LED(dim_gpio, pin_factory=native_factory)  # assign lightingLedMain
        self.main_lighting_dim = dim_value

    def on(self):
        """Powers on the main PWR, main LED and supplemental LED's at last set levels"""
        if not self.status:
            time.sleep(.5)
            self.main_lighting_led.on()
            self.status = True
            print('Lights on')

    def dim(self, dim_value=0):
        """Set the dim level for the main LED. The supplemental LED's are assigned based on the configuration file data
        as a percentage of the MainLED level"""
        self.main_lighting_led.value = dim_value
        print(dim_value)

    def off(self):
        """Powers off the main PWR, main LED and supplemental LED's at last set levels"""
        if self.status:
            self.main_lighting_led.off()
            self.status = False
            print('Lights off')
