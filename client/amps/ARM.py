import gpiozero
import time
from time import sleep
import logging


class ARM():
    '''ARM Class is to control the stepper motor using stepper controller DM322E

    gpioARMEna: set the raspberry pi pin for Enable on controller
    gpioARMDir: set the raspberry pi pin for Direction on controller
    gpioARMPul: set the raspberry pi pin for Pulse on controller
    gpioARMEndL: set the raspberry pi pin for Left Limit Sensor on controller
    gpioARMEndR: set the raspberry pi pin for Right Limit Sensor on controller
    '''
    ARMSleepTime = 0.0000025  # internal sleep variable

    def __init__(self, gpioARMEna, gpioARMDir, gpioARMPul, gpioARMEndL, gpioARMEndR, ARMLoc=0, ARML2RTotalStps=100000, ARMRevolution=400):
        self.ARMPins = [gpioARMEna, gpioARMDir, gpioARMPul]
        self.ARMEna = gpiozero.OutputDevice(gpioARMEna)
        self.ARMDir = gpiozero.OutputDevice(gpioARMDir)
        self.ARMPul = gpiozero.OutputDevice(gpioARMPul)
        self.ARMEndL = gpiozero.InputDevice(gpioARMEndL, pull_up=True)
        self.ARMEndR = gpiozero.InputDevice(gpioARMEndR, pull_up=True)
        self.ARMLoc = ARMLoc
        self.ARML2RTotalStps = ARML2RTotalStps
        self.ARMRevolution = ARMRevolution

    def Callibrate(self):
        '''Callibration routine to set the zero position and max step position.
        Note: zero postion gets callibrated everytime left proximity is triggered.'''
        # While State
        while ( self.ARMEndL.is_active == False):
            

            self.Pulsate(dir='L')
        # LEDMAIN(Alert)
        self.ARML2RTotalStps = 0
        self.ARMLoc = 0
        sleep(1)

        logging.INFO('Far Left Reached')
        while(self.ARMEndR.is_active == False):

            self.Pulsate(dir='R')
            self.ARML2RTotalStps += 1
            self.ARMLoc += 1
        # LEDMAIN(Alert)

        # moveTo(pos=0)
        # LEDMAIN(Homage)

    def Pulsate(self, dir):
        '''to move the stepper one step in a direction assigned every time it is called'''
        # self.ARMEna.on()
        if dir == 'L':

            if (self.ARMEndL.is_active == False):  # Check if ARM has reached far left

                if self.ARMDir.is_active == False:  # check the status of direction pin and set it accordingly
                    sleep(0.25)
                    self.ARMDir.on()
                    sleep(0.25)
                    # set pulse pin on and off
                sleep(ARM.ARMSleepTime)
                self.ARMPul.off()
                sleep(ARM.ARMSleepTime)
                self.ARMPul.on()
                # print('going L')
                self.ARMLoc -= 1
            elif(self.ARMEndL.is_active == True):
                print('Reached the far left limit')
                



        elif dir == 'R':
            if (self.ARMEndR.is_active == False):
                if self.ARMDir.is_active == True:
                    sleep(ARM.ARMSleepTime)
                    self.ARMDir.off()
                    sleep(ARM.ARMSleepTime)

                sleep(ARM.ARMSleepTime)
                self.ARMPul.off()
                sleep(ARM.ARMSleepTime)
                self.ARMPul.on()
                self.ARMLoc += 1
            elif (self.ARMEndR.is_active == True):
                print('Reached the far right limit')


                

        else :
            print ('Direction ')



    def goToLoc(self, location, speed=100):

        if location != 0:
            actualSteps = int((location * self.ARML2RTotalStps)/100)
        else:
            actualSteps = 0
        
        print()

        if actualSteps > self.ARMLoc :
            while actualSteps >=  self.ARMLoc :
                self.Pulsate(dir='R')

        elif actualSteps < self.ARMLoc:
            while actualSteps <= self.ARMLoc:
                self.Pulsate(dir='L')

    def toHome(self):
        self.goToLoc(0)
