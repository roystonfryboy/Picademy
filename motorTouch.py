import explorerhat
from time import sleep

from random import randint

def wheel (channel, event):
    duration = randint(1,10)
    
    print (duration)
    if duration < 6:
        print ("Too slow")
    else:
        print ("Fast")
    explorerhat.motor.one.forward(randint(50,100))
    sleep(5)
    explorerhat.motor.one.stop()

def wheel2 (channel, event):
    duration = randint(1,10)
    print (duration)
    if duration < 8:
        print ("if you are going backwards go faster than that")
    else:
        print ("better")
    explorerhat.motor.one.backward(randint(20,100))
    sleep(5)
    explorerhat.motor.one.stop()

explorerhat.touch.one.pressed(wheel)

explorerhat.touch.two.pressed(wheel2)
