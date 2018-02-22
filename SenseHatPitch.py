from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

for i in range (5):

    data = sense.get_orientation()
    pitch = data ["pitch"]
    sleep(1)

    print (pitch)

    sense.show_message(str(pitch))
