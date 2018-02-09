import explorerhat
from time import sleep

explorerhat.motor.one.forward(100)

sleep(3)

explorerhat.motor.one.stop()

explorerhat.motor.one.backwards(100)

sleep(3)

explorerhat.motor.one.stop()
