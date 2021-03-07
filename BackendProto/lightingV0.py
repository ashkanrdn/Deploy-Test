import gpiozero
from gpiozero import DigitalOutputDevice
from gpiozero import PWMLED
import time

#TEMPORARY GPIO ASSIGNMENTS UNTIL CONFIG FILE COMPLETE
gpioledODMainPwr = 18 #MAIN PWR GPIO ASSIGNMENT
gpioledPWMMainDim = 25 #MAIN LED GPIO ASSIGNMENT
gpioledPWMSuppOneDim = 13 #SUPP 1 LED GPIO ASSIGNMENT
gpioLedPWMSuppTwoDim = 12 #SUPP 2 LED GPIO ASSIGNMENT
gpioODPul = 21 #STEPPER PULSE GPIO ASSIGNMENT
gpioODDir = 24 #STEPPER DIRECTION GPIO ASSIGNMENT
gpioODEnable = 10 #STEPPER ENABLE GPIO ASSIGNMENT
gpioIDendArmLt = 8 #PROXIMITY LEFT SENSOR ASSIGNMENT
gpioIDendArmRt = 11 #PROXIMITY RIGHT GPIO ASSIGNMENT
ledSuppOnePercentage = 0.50 #Supplemental One LED percentage of main from calibration
ledSuppTwoPercentage = 0.50 #Supplemental Two LED percentage of main from calibration

#Lighting Control Basic Function

#ledMain is the main glow light class 
#it inherets the PMWLED gpiozero class and adds functionality to 
#power on the main led before dimming and power off the main power when turning off

class LedMain(PWMLED):
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

    def __init__(self, gpioPwr, gpioDim, gpioSupp1, gpioSupp2):
        super().__init__(gpioDim) #inherit PMWLED class
        self.power = gpiozero.DigitalOutputDevice(gpioPwr) #assign MainLED power on/off
        self.ledSuppOne = gpiozero.PWMLED(gpioSupp1) #assign suppOne as PWMLED
        self.ledSuppTwo = gpiozero.PWMLED(gpioSupp2) #assign suppTwo as PWMLED

    def on(self):
        '''Powers on the main PWR, main LED and supplemental LED's at last set levels'''
        self.power.on()
        time.sleep(.5)
        self.on()
        self.ledSuppOne.on()
        self.ledSuppTwo.on()

    def dim(self,level):
        '''Set the dim level for the main LED. The supplemental LED's are asigned based on the configuration file data as a percentage of the MainLED level'''
        if self.power.is_active == False:
            self.power.on()
        self.value = level
        self.ledSuppOne.value = (level * ledSuppOnePercentage)
        self.ledSuppTwo.value = (level * ledSuppTwoPercentage)
        self.on()
        self.ledSuppOne.on()
        self.ledSuppTwo.on()
  
    def off(self):
        '''Powers off the main PWR, main LED and supplemental LED's at last set levels'''
        self.off()
        self.ledSuppOne.off()
        self.ledSuppTwo.off()
        time.sleep(0.5)
        self.power.off()
   
ledGrow = LedMain(gpioledODMainPwr, gpioledPWMMainDim,gpioledPWMSuppOneDim, gpioLedPWMSuppTwoDim)




