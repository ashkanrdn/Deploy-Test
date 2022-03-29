import datetime
import gpiozero
from time import sleep
from os.path import dirname, join, abspath
import sys
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
import appConfig 



class ARM():
    '''ARM Class is to control the stepper motor using stepper controller DM322E

    gpioARMEna: set the raspberry pi pin for Enable on controller
    gpioARMDir: set the raspberry pi pin for Direction on controller
    gpioARMPul: set the raspberry pi pin for Pulse on controller
    gpioARMEndL: set the raspberry pi pin for Left Limit Sensor on controller
    gpioARMEndR: set the raspberry pi pin for Right Limit Sensor on controller
    '''
    ARMSleepTime = 0.00000025  # internal sleep variable

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
        print("Calibrating")
        while ( self.ARMEndL.is_active == False):
            # print("Not at left limit moving towards the limit")
            self.Pulsate(dir='L')
            self.ARMLoc = 0
        # LEDMAIN(Alert)
            self.ARML2RTotalStps = 0
        
        sleep(1)

        print('Far Left Reached')
        print(self.ARMLoc , "Arm LOC")
        while(self.ARMEndR.is_active == False):

            self.Pulsate(dir='R')
            self.ARML2RTotalStps += 1
            self.ARMLoc += 1
        # LEDMAIN(Alert)
        print("Going")
        print(self.ARMLoc, "Arm LOC")
        print(self.ARML2RTotalStps, 'total steps')
  
        # moveTo(pos=0)
        # LEDMAIN(Homage)

    def Pulsate(self, dir):
        '''to move the stepper one step in a direction (L or R) assigned every time it is called'''
        # self.ARMEna.on()
        if dir == 'L':
            #while (self.ARMEndL.is_active == False):  # Check if ARM has has room or reached left limit
            if self.ARMDir.is_active == False:  # check the status of direction pin and set it accordingly
                sleep(0.25)
                self.ARMDir.on()
                sleep(0.25)
            if self.ARMEndL.is_active == True:
                self.ARMLoc = 0
                print(self.ARMLoc," Reached far left limit")
            # one pulse to left
            sleep(ARM.ARMSleepTime)
            self.ARMPul.off()
            sleep(ARM.ARMSleepTime)
            self.ARMPul.on()
            self.ARMLoc -= 1
            
                
            # print(self.ARMLoc)
        elif dir == 'R':
            # print(self.ARMLoc)
           # while (self.ARMEndR.is_active == False):

           #Check direction of arm
            if self.ARMDir.is_active == True:
                sleep(0.25)
                self.ARMDir.off()
                sleep(0.25)
            if self.ARMEndR.is_active == True:
                print('Reached the far right limit')
                print(self.ARMLoc)
            sleep(ARM.ARMSleepTime)
            self.ARMPul.off()
            sleep(ARM.ARMSleepTime)
            self.ARMPul.on()
            self.ARMLoc += 1
            #print('Arm Location', self.ARMLoc)
            
        else :
            print ('Direction')



    def goToLoc(self, location, speed=100):
        print('sent location value = ', location)
        
                

        if location < self.ARMLoc:
            while location >  self.ARMLoc :
                self.Pulsate(dir='R')
                print('Right location', self.ARMLoc)
        elif location > self.ARMLoc:
            while location < self.ARMLoc:
                self.Pulsate(dir='L')
                print('Left location', self.ARMLoc)

        else:
            location = 0
            while location < self.ARMLoc:
                self.Pulsate(dir='L')
                print('something is wrong')
        
        #self.ARMLoc = location
        #print('location', self.ARMLoc)

    def DaySwing(self, swingCount):
        '''Callibration routine to set the zero position and max step position.
        Note: zero postion gets callibrated everytime left proximity is triggered.'''
        # While State
        print("DaySwing")
        while ( self.ARMEndL.is_active == False):
            # print("Not at left limit moving towards the limit")
            self.Pulsate(dir='L')
            self.ARMLoc = 0
        # LEDMAIN(Alert)
            self.ARML2RTotalStps = 0
        
        sleep(1)

        print('Far Left Reached')
        print(self.ARMLoc , "Arm LOC")
        print('Moving Right', datetime.datetime.now())
        #calculate timing based on 1369550 total steps
        while ( self.ARMEndR.is_active == False):
       # for i in range(swingCount):
            self.Pulsate('R')
            sleepTimeDaySwing = swingCount/1369550
            sleep(sleepTimeDaySwing)
        print('End Light Day')


        # while(self.ARMEndR.is_active == False):

        #     self.Pulsate(dir='R')
        #     self.ARML2RTotalStps += 1
        #     self.ARMLoc += 1

        self.ARMSleepTime = 0.00000025    
        # LEDMAIN(Alert)
        print("Going")
        print(self.ARMLoc, "Arm LOC")   

    def toHome(self):
        self.goToLoc(0)

       



gpioARMEna = 10
gpioARMDir = 24
gpioARMPul = 21
gpioARMEndL = 8
gpioARMEndR = 11

# ARMControls = ARM(gpioARMEna, gpioARMDir, gpioARMPul, gpioARMEndL, gpioARMEndR)

