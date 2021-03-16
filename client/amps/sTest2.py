import gpiozero
import time

pulse = gpiozero.OutputDevice(21)
direction = gpiozero.OutputDevice(24)

direction.off()
pulse.off()
time.sleep(1)
count = 0
#speed in determined by pause between on and off. 0.0000025 second is fastest. use that as constant (pauseTime) and divide to slow down.
pauseTime = 0.0000025
#run stepper forward. 1600 steps is one full rotation. 
def move(move):

    while move == True:
        pulse.on()
        time.sleep(pauseTime)
        pulse.off()
        time.sleep(pauseTime)
        
    
time.sleep(.25)
# direction.on()
# time.sleep(.25)
# for i in (range((1600*10))):

#     #time.sleep(1)
#     pulse.on()
#     time.sleep(pauseTime)
#     pulse.off()
#     time.sleep(pauseTime)
#     count = count +1
# time.sleep(.25)
# direction.off()
# pulse.off()
# print(count)

move(True)
time.sleep(5)
move(False)