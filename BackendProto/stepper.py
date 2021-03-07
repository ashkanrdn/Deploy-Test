import gpiozero
import time
from time import sleep



class Stepper():
    def __init__(self, gpioEna, gpioDir, gpioPul):
        self.pins = [gpioEna, gpioDir, gpioPul]
        self.enable = gpiozero.OutputDevice(gpioEna)
        self.direction = gpiozero.OutputDevice(gpioDir)
        self.pulse = gpiozero.OutputDevice(gpioPul)
        self.location = 0

    def Callibrate(self):
        self.location = 0

    def Left(self, steps, speed = 100):
        pause = (0.00025)/speed
        sleep(0.25)
        self.direction.on()
        sleep(0.25)
        count = 0
        for i in range(steps):
            #if 
            self.pulse.off()
            sleep(pause)
            self.pulse.on()
            sleep(pause)
            self.location = self.location - 1
        print(self.location)
        self.pulse.off()

    def Right(self, steps, speed=100):
        pause = (0.00025)/speed
        sleep(0.25)
        self.direction.off()
        sleep(0.25)
        count = 0
        for i in range(steps):
            self.pulse.off()
            sleep(pause)
            self.pulse.on()
            sleep(pause)
            self.location = self.location + 1
        print(self.location)
        
        self.pulse.off()
   


sleep(1)
stepper = Stepper(23,24,21)
stepper.Callibrate()
stepper.Right(1600)
stepper.Left(1600)


        

