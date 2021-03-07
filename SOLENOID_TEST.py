import gpiozero
from gpiozero import DigitalOutputDevice
import time

class Solenoid(DigitalOutputDevice):
    def __init__(self, guid):
        super().__init__(guid)
    def timedon(self, t):
        self.on()
        time.sleep(t)
        self.off()


pump = DigitalOutputDevice(26)
waterSolenoid = Solenoid(27)
nutrientSolenoid = Solenoid(17)
levelOneSolenoid = Solenoid(22)
levelTwoSolenoid = Solenoid(10)
levelThreeSolenoid = Solenoid(9)
levelFourSolenoid = Solenoid(11)
levelFiveSolenoid = Solenoid(0)

# waterSolenoid.timedon(3)
# nutrientSolenoid.timedon(4)
# levelOneSolenoid.timedon(2)
# levelTwoSolenoid.timedon(2)
# levelThreeSolenoid.timedon(2)
# levelFourSolenoid.timedon(2)
# levelFiveSolenoid.timedon(2)

def waterCycle(solenoids, cycleTime):
    pump.on()
    time.sleep(1)
    waterSolenoid.on()
    time.sleep(1)
    for i in solenoids:
        i.on()
        time.sleep(cycleTime)
        i.off()
    time.sleep(1)
    waterSolenoid.off()
    time.sleep(1)
    pump.off()

levels = [levelOneSolenoid,levelTwoSolenoid,levelThreeSolenoid,levelFourSolenoid,levelFiveSolenoid]
waterCycle(levels, 2)




