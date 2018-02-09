from twython import Twython
from sense_hat import SenseHat
from time import sleep
from picamera import PiCamera
import os


from auth import (
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )

twitter = Twython(
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )

def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))
    return(t)

def get_photo():
    camera.start_preview(alpha=192)
    sleep(1)
    camera.capture("/home/pi/Desktop/team.jpg")
    camera.stop_preview()

def get_message():
    temp = sense.get_temperature()
    humid = sense.get_humidity()
    cpu_temp = get_cpu_temp()
    correct_temp = temp - ((cpu_temp - temp)/1.5)
    correct_temp1 = correct_temp
    message =  'Temperature is : ' + str(round(correct_temp,1)) + chr(176) + "C" +'\n'
    message =  message + 'Humidity is : ' + str(round(humid,1)) +'%'
    return message,correct_temp


sense = SenseHat()
camera = PiCamera()
while True:
    get_photo()
    message,temp =  get_message()
    
    message = "#Picademy! \n" +message
    media_ids = []
    with open('/home/pi/Desktop/team.jpg', 'rb') as f:
            response = twitter.upload_media(media=f)
    media_ids.append(response['media_id'])
    twitter.update_status(status=message, media_ids=media_ids)
    #with open('/home/pi/Desktop/team.jpg', 'rb') as photo: twitter.update_status_with_media(status=message, media=photo)

    print("Tweeted: %s" % message)
    message,temp = get_message()
    print (temp)

    if temp > 20:
        sense.clear(255, 0, 0)
        sleep(2)
        sense.clear()
        sense.show_message("Hot Dam Hot")
    else:
        sense.clear(0,0,255)
        sleep(2)
        sense.clear()
        sense.show_message("just chilling")

    sleep(600)
