import gpiozero
import time
from time import sleep






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

    def __init__(self, gpioPwr, gpioDim, gpioSupp1, gpioSupp2, ledSuppOneDim = 0.5, ledSuppTwoDim = 0.5 , ledMainDim = 0.5):

        self.lightingLedMainPWR = gpiozero.DigitalOutputDevice(gpioPwr) #assign MainLED power on/off
        self.lightingLedMain = gpiozero.PWMLED(gpioDim) #assign lightingLedMain
        self.lightingLedSuppOne = gpiozero.PWMLED(gpioSupp1) #assign lightingLedSuppOne as PWMLED
        self.lightingLedSuppTwo = gpiozero.PWMLED(gpioSupp2) #assign lightingLedSuppTwo as PWMLED
        self.lightingLedSuppOneDim = ledSuppOneDim # setting the initial Dim value for lightingLedSuppOne
        self.lightingLedSuppTwoDim =ledSuppTwoDim #setting the initial Dim value for lightingLedSuppTwo
        # print('Class Initiated')
    def on(self):
        '''Powers on the main PWR, main LED and supplemental LED's at last set levels'''
        self.lightingLedMainPWR.on()
        time.sleep(.5)
        # self.lightingLedMain.on()
        self.lightingLedSuppOne.on()
        self.lightingLedSuppTwo.on()
     

    def dim(self,mainDim=0,sup1Dim=0,sup2Dim=0):
        '''Set the dim level for the main LED. The supplemental LED's are asigned based on the configuration file data as a percentage of the MainLED level'''
        if self.lightingLedMainPWR.is_active == False:
            self.lightingLedMainPWR.on()
     

        self.lightingLedMain.value = mainDim
        self.lightingLedSuppOne.value = sup1Dim
        self.lightingLedSuppTwo.value = sup2Dim


   

    def off(self):
        '''Powers off the main PWR, main LED and supplemental LED's at last set levels'''
        self.lightingLedMain.off()
        self.lightingLedSuppOne.off()
        self.lightingLedSuppTwo.off()

        self.lightingLedMainPWR.off()
  




    def Callibrate(self, suppOneLevel,suppTwoLevel):
        #figure out how to callibrate supp leds
        self.lightingLedMainPWR.power.on()

        #set supplemental one level:
        self.lightingLedSuppOne.value = suppOneLevel
        self.lightingLedSuppTwo.value = suppTwoLevel
        self.ledSuppOnePercentage = (self.lightingLedSuppOne.value/self.lightingLedMain)
        self.ledSuppTwoPercentage = (self.lightingLedSuppTwo.value/self.lightingLedMain)
