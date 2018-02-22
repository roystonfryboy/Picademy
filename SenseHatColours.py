#Test Sense Hat
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0,)
blue = (0,0,255)

for i in range(5):
    sense.clear(red)
    sleep(1)
    sense.clear()
    sleep(1)
    sense.clear(blue)


