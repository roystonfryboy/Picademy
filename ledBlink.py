#led and buzzer

from gpiozero import LED

from gpiozero import Buzzer

from time import sleep


led =LED(17)
led1 = LED(27)
buz = Buzzer(24)

led.blink(0.5, 0.5, 5, False)
buz.on
sleep(1)
buz.off
led1.blink(0.5,0.5, 5, False)
