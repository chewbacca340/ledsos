import RPi.GPIO as gpio
#led is on 18
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18,gpio.OUT)

gpio.output(18,1)
print "led on"
time.sleep(3)
gpio.output(18,0)
print "led off"
