import gpiozero
import time

# Test
hello = 55555
test = gpiozero.OutputDevice(21)

delay = 0.0000001

# dir = gpiozero.OutputDevice(21)
# dir.on()
time.sleep(0.1)
for i in range(1600):

    test.on()
    time.sleep(0.0000025)

    test.off()

    time.sleep(delay)

dir.off()
time.sleep(0.1)
for i in range(1600):

    test.on()
    time.sleep(0.0000025)

    test.off()

    time.sleep(delay)
    # break

    # for i in range(6400):
    #     time.sleep(delay)
    #     pul.
