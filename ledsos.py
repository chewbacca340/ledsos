import RPi.GPIO as gpio
#led is on 18
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18,gpio.OUT)

for x in range(0, 3):
  gpio.output(18,1)
  #print "led on"
  time.sleep(1)
  gpio.output(18,0)
  #print "led off"
  time.sleep(1)

for x in range(0, 3):
  gpio.output(18,1)
  time.sleep(3)
  gpio.output(18,0)
  time.sleep(1)

for x in range(0,3):
  gpio.output(18,1)
  time.sleep(1)
  gpio.output(18,0)
