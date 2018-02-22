#selfie
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=192)
sleep(3)
camera.capture("/home/pi/selfie.jpg")
camera.stop_preview()
