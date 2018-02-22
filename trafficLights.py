#Traffic Lights
from gpiozero import TrafficLights
from time import sleep

lights = TrafficLights(21,20,16)

lights.red.on()
sleep(3)
lights.red.off()
lights.amber.on()
sleep(3)
lights.amber.off()
sleep(3)
lights.green.on()
sleep(3)
lights.green.off()
