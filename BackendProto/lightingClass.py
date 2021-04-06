import gpiozero
import time
from time import sleep

#TEMPORARY GPIO ASSIGNMENTS UNTIL CONFIG FILE COMPLETE
gpioledODMainPwr = 22#18
gpioledPWMMainDim = 18#22
gpioledPWMSuppOneDim = 13
gpioLedPWMSuppTwoDiM = 12
gpioODPul = 21
gpioODDir = 24
gpioODEnable = 10
gpioIDendArmLt = 8
gpioIDendArmRt = 11



class Stepper():
    '''Stepper Class is to control the stepper motor using stepper controller DM322E
    
    gpioEna: set the raspberry pi pin for Enable on controller
    gpioDir: set the raspberry pi pin for Direction on controller
    gpioPul: set the raspberry pi pin for Pulse on controller
    gpioEndLt: set the raspberry pi pin for Left Limit Sensor on controller
    gpioEndRt: set the raspberry pi pin for Right Limit Sensor on controller
    '''
    def __init__(self, gpioEna, gpioDir, gpioPul, gpioEndLt, gpioEndRt):
        self.pins = [gpioEna, gpioDir, gpioPul]
        self.enable = gpiozero.OutputDevice(gpioEna)
        self.direction = gpiozero.OutputDevice(gpioDir)
        self.pulse = gpiozero.OutputDevice(gpioPul)
        self.endLeft = gpiozero.InputDevice(gpioEndLt)
        self.endRight = gpiozero.InputDevice(gpioEndRt)
        self.location = 0
        self.maxStep = 100000

    
    
    def Callibrate(self):
        '''Callibration routine to set the zero position and max step position.
        Note: zero postion gets callibrated everytime left proximity is triggered.'''
        self.Left(1000000)
        self.Right(100000)
        self.maxStep = self.location
        self.location = 1

    def toLocation(self,toPosition, speed = 100):
        ''' Move the swing arm to desired location as a percentage along the entire distance
        toPosition: the step location to move the arm as a percentage of total(0-100)
        speed: default = 100, set between 1-100'''
        if toPosition ==0:
            moveTo = 0
        else:
            moveTo = int((toPosition/100) * self.maxStep)
        
        if moveTo == self.location:
           print("already there") 
        elif moveTo < self.location:
            self.Left((self.location - moveTo), speed)
        elif moveTo > self.location:
            self.Right((moveTo - self.location), speed)


    def Left(self, steps, speed = 100):
        '''Move arm left a desired number of motor steps.
        steps: how many motor steps to move, 1600 steps is one rotation
        speed: how fast to move between 1 and 100'''
        if speed <= 0:
            speed = 1
        elif speed > 200:
            speed = 200
        pause = (0.00025)/speed
        if self.direction.is_active == False:
            sleep(0.25)
            self.direction.on()
            sleep(0.25)
        for i in range(steps):
            if self.endLeft.is_active == False:
                self.pulse.off()
                sleep(pause)
                self.pulse.on()
                sleep(pause)
                self.location = self.location - 1
            else:
                self.location = 0
                print("reached far left")
        print(self.location)
        self.pulse.off()

    def Right(self, steps, speed=100):
        '''Move arm right a desired number of motor steps.
        steps: how many motor steps to move, 1600 steps is one rotation
        speed: how fast to move between 1 and 100'''
        if speed <= 0:
            speed = 1
        elif speed > 200:
            speed = 200
        pause = (0.00025)/speed
        if self.direction.is_active == True:
            sleep(0.25)
            self.direction.off()
            sleep(0.25)
        for i in range(steps):
            if self.endLeft.is_active == False:
                self.pulse.off()
                sleep(pause)
                self.pulse.on()
                sleep(pause)
                self.location = self.location + 1
            else:
                print("reached far right, please recallibrate")
        print(self.location)
        
        self.pulse.off()
    
    def toHome(self):
        '''Move the arm to the dock location'''
        self.toLocation(0)

class LedMain(gpiozero.PWMLED):
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

    def __init__(self, gpioPwr, gpioDim, gpioSupp1, gpioSupp2, ledSuppOnePercentage = 0.50, ledSuppTwoPercentage = 0.50):
        super().__init__(gpioDim) #inherit PMWLED class
        self.power = gpiozero.DigitalOutputDevice(gpioPwr) #assign MainLED power on/off
        self.ledSuppOne = gpiozero.PWMLED(gpioSupp1) #assign suppOne as PWMLED
        self.ledSuppTwo = gpiozero.PWMLED(gpioSupp2) #assign suppTwo as PWMLED
        self.ledSuppOnePercentage = ledSuppOnePercentage
        self.ledSuppTwoPercentage = ledSuppTwoPercentage

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
        self.ledSuppOne.value = (level * self.ledSuppOnePercentage)
        self.ledSuppTwo.value = (level * self.ledSuppTwoPercentage)
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
    def Callibrate(self, suppOneLevel = 50,suppTwoLevel = 50):
        #figure out how to callibrate supp leds
        self.power.on()
        self.dim(100)
        #set supplemental one level:
        self.ledSuppTwo.value = suppOneLevel
        self.ledSuppTwo.value = suppTwoLevel
        self.ledSuppOnePercentage = suppOneLevel
        self.ledSuppTwoPercentage = suppTwoLevel
 
class LightingArm():
    def __init__(self, gpioPwr, gpioDim, gpioSupp1, gpioSupp2, gpioEna, gpioDir, gpioPul, gpioEndLt, gpioEndRt):
        self.lights = LedMain(gpioPwr,gpioDim,gpioSupp1,gpioSupp2)
        self.stepper = Stepper(gpioEna,gpioDir,gpioPul,gpioEndLt,gpioEndRt)
    # def CallibrateLights(self, suppOneLevel = 50, suppTwoLevel):
    #     self.lights.Callibrate(suppOneLevel,suppTwoLevel)
    # def CallibrateArm(self)
    #     self.stepper.Callibrate()
    def on(self):
        self.lights.on()
    def dim(self, dimSetting):
        self.lights.dim(dimSetting)
    def off(self):
        self.lights.off()
    def moveTo(self, position, ledOn = True):
        if ledOn == True:
            self.on()
        elif ledOn == False:
            self.off()
        self.stepper.toLocation(position)
    def home(self):
        self.stepper.toHome()
        self.lights.off()
    def SweepLight(self, speed = 100):
        self.on()
        self.stepper.toLocation(100,speed)
        self.stepper.toLocation(0,speed)


    


#testing functionality
test = LedMain(gpioledODMainPwr,gpioledPWMMainDim,gpioledPWMSuppOneDim,gpioLedPWMSuppTwoDiM)
test.dim(1)
print(test.value)
time.sleep(5)
