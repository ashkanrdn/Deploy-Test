import gpiozero
import time
from time import sleep

#TEMPORARY GPIO ASSIGNMENTS UNTIL CONFIG FILE COMPLETE
gpioledODMainPwr = 18
gpioledPWMMainDim = 25
gpioledPWMSuppOneDIm = 13
gpioLedPWMSuppTwoDIM = 12
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
        self.left(1000000)
        self.right(100000)
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
        self.toLocation(0)

   

#testing functionality
sleep(1)
stepper = Stepper(gpioODEnable,gpioODDir,gpioODPul,gpioIDendArmLt,gpioIDendArmRt)
stepper.Right(12800)
stepper.Right(1600)
stepper.Left(12800, 50)
stepper.toLocation(50)
#button push while loop might look like this
count = 1
while True:
    count = count + 1
    stepper.Left(10,200)
    if count > 600:
        break

stepper.toHome()
