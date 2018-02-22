#Test Sense Hat
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = (255, 0, 0,)
w = (255, 255, 255)


for i in range(3):
    sense.clear(r)
    sleep(1)
    sense.clear(w)
    sleep(1)
    sense.clear(r)
    sleep(1)

pic = [
    w, w, r, r, r, w, w, w,
    w, r, w, w, w, r, w, w,
    r, w, w, w, w, r, w, w,
    r, w, w, w, w, r, w, w,
    r, w, w, w, r, w, w, w,
    r, w, w, w, w, r, w, w,
    w, r, w, w, w, w, r, w,
    w, w, r, r, r, r, w, w,
    ]

pic2 = [
    w, w, w, r, r, w, w, w,
    w, r, w, w, w, r, w, w,
    r, w, w, w, w, r, w, w,
    r, w, w, w, w, r, w, w,
    r, w, w, w, r, w, w, w,
    r, w, w, w, w, r, w, w,
    w, r, w, w, w, w, r, w,
    w, w, w, w, w, w, w, w,
    ]


sense.set_pixels(pic)
sleep (2)
sense.clear()
sense.set_pixels(pic2)
sleep (2)
sense.clear()


