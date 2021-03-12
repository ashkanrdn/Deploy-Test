import gpiozero
from gpiozero import DigitalOutputDevice
import time

#Plumbing Control BAsic Functions



class Solenoid(gpiozero.OutputDevice):
    def __init__(self, guid):
        super().__init__(guid)
    def timedon(self, t):
        self.on()
        time.sleep(t)
        self.off()

#Assign GPIO's refer to master list

pumpPWR = DigitalOutputDevice(7)
waterSolenoid = Solenoid(22)
nutrientSolenoid = Solenoid(23)
levelOneSolenoid = Solenoid(27)
levelTwoSolenoid = Solenoid(17)
levelThreeSolenoid = Solenoid(3)
levelFourSolenoid = Solenoid(15)
levelFiveSolenoid = Solenoid(4)
#transferSolenoid = Solenoid()

#solenoidTimeOpen =

def waterCycle(solenoids, cycleTime):

    #need to add a constant check for tank level
    #if it hits empty stop cycle
    pumpPWR.on()
    time.sleep(1)
    waterSolenoid.on()
    time.sleep(1)
    for i in solenoids:
    #check tank levels

        i.timedon(cycleTime)
    time.sleep(1)
    waterSolenoid.off()
    time.sleep(1)
    pumpPWR.off()

    #check tank levels

    #check tank levels

def nutrientCycle(solenoids, cycleTime):

    #check tank levels

    pumpPWR.on()
    time.sleep(1)
    nutrientSolenoid.on()
    time.sleep(1)
    for i in solenoids:
        i.timedon(cycleTime)
    time.sleep(1)
    nutrientSolenoid.off()
    time.sleep(1)
    pumpPWR.off()

def tankTransfer():
    #check tank levels
    transferSolenoid.on()
    #need to figure out how long valve shoudl stay open for transfer
    time.sleep(XXX)
    transferSolenoid.off()
    #check tank levels




levels = [levelOneSolenoid,levelTwoSolenoid,levelThreeSolenoid,levelFourSolenoid,levelFiveSolenoid]


#Test the fucntions
waterCycle(levels, 2)
nutrientCycle(levels, 2)



