#flashing LED

from gpiozero import LED
from time import sleep

myled = LED(17)
myled1 = LED(6)
buzz = LED(24)

while True:
    myled.on()
    sleep(1)
    myled.off()
    sleep(1)
    myled1.on()
    sleep(1)
    myled1.off
    sleep(1)
    buzz.on()
    sleep(1)
    buzz.off
    sleep(1)
    
