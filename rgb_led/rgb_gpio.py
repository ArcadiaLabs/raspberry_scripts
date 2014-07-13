#!/usr/bin/env python2.7  
# Using PWM with RPi.GPIO pt 2 - requires RPi.GPIO 0.5.2a or higher  
  
import RPi.GPIO as GPIO # always needed with RPi.GPIO  
from time import sleep  # pull in the sleep function from time module  
  
GPIO.setmode(GPIO.BOARD)  # choose BCM or BOARD numbering schemes. I use BOARD  

red = 11 # set pin 11 (GPIO 0) for red led
green = 13 # set pin 13 (GPIO 2) for green led 
blue = 15 # set pin 15 (GPIO 3) for blue led
  
GPIO.setup(red, GPIO.OUT) # set red led pin as output
GPIO.setup(green, GPIO.OUT) # set green led pin as output
GPIO.setup(blue, GPIO.OUT) # set blue led pin as output
  
GPIO.output(red, 1) 
GPIO.output(green, 1) 
GPIO.output(blue, 1)
  
pause_time = 0.5 # you can change this to slow down/speed up  
  
try:  
    while True:
	GPIO.output(red, 1)
	GPIO.output(green, 0)
	GPIO.output(blue, 0)    
    	sleep(pause_time)  

	GPIO.output(red, 1)
        GPIO.output(green, 1)
        GPIO.output(blue, 0)
        sleep(pause_time)

	GPIO.output(red, 1)
        GPIO.output(green, 0)
        GPIO.output(blue, 1)
        sleep(pause_time)

	GPIO.output(red, 0)
        GPIO.output(green, 1)
        GPIO.output(blue, 0)
        sleep(pause_time)

	GPIO.output(red, 0)
        GPIO.output(green, 1)
        GPIO.output(blue, 1)
        sleep(pause_time)

	GPIO.output(red, 0)
        GPIO.output(green, 0)
        GPIO.output(blue, 1)
        sleep(pause_time)

	GPIO.output(red, 1)
        GPIO.output(green, 1)
        GPIO.output(blue, 1)
        sleep(pause_time)	
  
except KeyboardInterrupt:  
    GPIO.output(red, 0)
    GPIO.output(green, 0)
    GPIO.output(blue, 0)
    GPIO.cleanup()          # clean up GPIO on CTRL+C exit 
