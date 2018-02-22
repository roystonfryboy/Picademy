from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    temp = sense.get_temperature()
    print (round(temp,2))

    if temp > 27:
        sense.clear(255, 0, 0)
        sleep(2)
        sense.clear()
        sense.show_message("Hot Dam Hot")
    else:
        sense.clear(0,0,255)
        sleep(2)
        sense.clear()
        sense.show_message("just chilling")

    sleep(5)
