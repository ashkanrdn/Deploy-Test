import gpiozero
import time
from time import sleep




class Stepper():
    '''Stepper Class is to control the stepper motor using stepper controller DM322E

    gpioEna: set the raspberry pi pin for Enable on controller
    gpioDir: set the raspberry pi pin for Direction on controller
    gpioARMPls: set the raspberry pi pin for Pulse on controller
    gpioEndLt: set the raspberry pi pin for Left Limit Sensor on controller
    gpioEndRt: set the raspberry pi pin for Right Limit Sensor on controller
    '''
    def __init__(self, gpioEna, gpioDir, gpioARMPls, gpioEndLt, gpioEndRt,ARMRevolution=400):
        self.ARMPins = [gpioEna, gpioDir, gpioARMPls]
        self.ARMNbl = gpiozero.OutputDevice(gpioEna)
        self.ARMDir = gpiozero.OutputDevice(gpioDir)
        self.ARMPls = gpiozero.OutputDevice(gpioARMPls)
        self.ARMEndL = gpiozero.InputDevice(gpioEndLt)
        self.ARMEndR = gpiozero.InputDevice(gpioEndRt)
        self.ARMLoc = 0
        self.ARML2RTotalStps = 100000
        self.ARMRevolution = ARMRevolution



    def Callibrate(self):
        '''Callibration routine to set the zero position and max step position.
        Note: zero postion gets callibrated everytime left proximity is triggered.'''
        self.Left(1000000) #
        self.Right(100000)
        self.ARML2RTotalStps = self.ARMLoc
        self.ARMLoc = 1

    def toLocation(self,toPosition, speed = 100):
        ''' Move the swing arm to desired ARMLoc as a percentage along the entire distance
        toPosition: the step ARMLoc to move the arm as a percentage of total(0-100)
        speed: default = 100, set between 1-100'''
        if toPosition ==0:
            moveTo = 0
        else:
            moveTo = int((toPosition/100) * self.ARML2RTotalStps)

        if moveTo == self.ARMLoc:
           print("already there")
        elif moveTo < self.ARMLoc:
            self.Left((self.ARMLoc - moveTo), speed)
        elif moveTo > self.ARMLoc:
            self.Right((moveTo - self.ARMLoc), speed)


    def Left(self, steps, speed = 100):
        '''Move arm left a desired number of motor steps.
        steps: how many motor steps to move, 400 steps is one rotation
        speed: how fast to move between 1 and 100'''
        if speed <= 0:
            speed = 1
        elif speed > 200:
            speed = 200
        pause = (0.00025)/speed
        if self.ARMDir.is_active == False:
            sleep(0.25)
            self.ARMDir.on()
            sleep(0.25)
        for i in range(steps):
            if self.ARMEndL.is_active == False:
                self.ARMPls.off()
                sleep(pause)
                self.ARMPls.on()
                sleep(pause)
                self.ARMLoc = self.ARMLoc - 1
            else:
                self.ARMLoc = 0
                print("reached far left")
        print(self.ARMLoc)
        self.ARMPls.off()

    def Right(self, steps, speed=100):
        '''Move arm right a desired number of motor steps.
        steps: how many motor steps to move, 400 steps is one rotation
        speed: how fast to move between 1 and 100'''
        if speed <= 0:
            speed = 1
        elif speed > 200:
            speed = 200
        pause = (0.00025)/speed
        if self.ARMDir.is_active == True:
            sleep(0.25)
            self.ARMDir.off()
            sleep(0.25)
        for i in range(steps):
            if self.ARMEndL.is_active == False:
                self.ARMPls.off()
                sleep(pause)
                self.ARMPls.on()
                sleep(pause)
                self.ARMLoc = self.ARMLoc + 1
            else:
                print("reached far right, please recallibrate")
        print(self.ARMLoc)

        self.ARMPls.off()

    def toHome(self):
        '''Move the arm to the dock ARMLoc'''
        self.toLocation(0)



# #testing functionality
# sleep(1)
# stepper = Stepper(gpioODEnable,gpioODDir,gpioODPul,gpioIDendArmLt,gpioIDendArmRt)
# stepper.Right(12800)
# stepper.Right(1600)
# stepper.Left(12800, 50)
# stepper.toLocation(50)
# #button push while loop might look like this
# count = 1
# while True:
#     count = count + 1
#     stepper.Left(10,200)
#     if count > 600:
#         break

# stepper.toHome()
