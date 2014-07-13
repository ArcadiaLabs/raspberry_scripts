#!/usr/bin/python3  
#Controlling a RGB LED with built in PWM.  
#Mostly copied from GPIO PWM example:  
#http://code.google.com/p/raspberry-gpio-python/wiki/PWM  
   
import time  
import RPi.GPIO as GPIO  
import math  
   
   
GPIO.setmode(GPIO.BOARD)  
red = 11 # set pin 11 (GPIO 0) for red led 
green = 13 # set pin 13 (GPIO 2) for green led  
blue = 15 # set pin 15 (GPIO 3) for blue led 

Freq = 100 #Hz     
   
GPIO.setup(red, GPIO.OUT) # setup all the pins  
GPIO.setup(green, GPIO.OUT)  
GPIO.setup(blue, GPIO.OUT)  
   
# setup all the colours  
RED = GPIO.PWM(red, Freq) #Pin, frequency  
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq) 

#Initial duty cycle of 0, so off  
RED.start(0) 
GREEN.start(0)    
BLUE.start(0)  
   
def colour(R, G, B, on_time):  
	# colour brightness range is 0-100  
	RED.ChangeDutyCycle(R)  
	GREEN.ChangeDutyCycle(G)  
	BLUE.ChangeDutyCycle(B)  
	time.sleep(on_time)  

	# turn everything off  
	RED.ChangeDutyCycle(0)  
	GREEN.ChangeDutyCycle(0)  
	BLUE.ChangeDutyCycle(0)  
   
def PosSinWave(amplitude, angle, frequency):  
	# angle in degrees  
	# creates a positive sin wave between 0 and amplitude*2  
	return amplitude + (amplitude * math.sin(math.radians(angle)*frequency) )  
   
try:       
	while 1:  
		for i in range(0, 720, 5):  
			colour( PosSinWave(50, i, 0.5),  
			PosSinWave(50, i, 1),  
			PosSinWave(50, i, 2),  
			0.1 )  
       
except KeyboardInterrupt:  
	# Stop all the PWM objects  
	RED.stop()  
	GREEN.stop()  
	BLUE.stop()  
	   
	# Tidy up and remaining connections.  
	GPIO.cleanup()  
