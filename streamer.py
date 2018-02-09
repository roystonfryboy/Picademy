from twython import TwythonStreamer
from twython import Twython
from time import sleep
from picamera import PiCamera
from sense_hat import SenseHat
import os
data1 = None



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

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        print('Hello')
        global data1
        data1= data
        print(data['id'])
        print(data['id_str'])
        print(data['user']['id'])
        print(data['user']['id_str'])
        print(data['text'])
        print(data['user']['name'])
        #twitter.update_status(status='More Testing')
        get_photo()
        message,temp =  get_message()
        
        message = "#Picademy! \nHi "+data['user']['name']+" here's the weather\n" +message
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

stream = MyStreamer(
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )
stream.statuses.filter(track='@PiWeather2')

#look for 'user':'id':
