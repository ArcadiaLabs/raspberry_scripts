#!/usr/bin/env python
 
# Import library functions we need
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)

# Setup software PWMs on the GPIO pins
PIN_RED = 11 # set pin 11 (GPIO 0) for red led
PIN_GREEN = 13 # set pin 13 (GPIO 2) for green led 
PIN_BLUE = 15 # set pin 15 (GPIO 3) for blue led
LED_MAX = 100

Freq = 100 #Hz

pause_time = 0.01           # you can change this to slow down/speed up 

GPIO.setup(PIN_RED, GPIO.OUT) # setup all the pins  
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_BLUE, GPIO.OUT)

#setup all the colours  
RED = GPIO.PWM(PIN_RED, Freq) #Pin, frequency  
GREEN = GPIO.PWM(PIN_GREEN, Freq)
BLUE = GPIO.PWM(PIN_BLUE, Freq)

#Initial duty cycle of 0, so off 
RED.start(0)  
GREEN.start(0)
BLUE.start(0)

# A function to set the colours
def SetLed(red, green, blue):
	RED.ChangeDutyCycle(int(red   * LED_MAX))
	GREEN.ChangeDutyCycle(int(green * LED_MAX))
	BLUE.ChangeDutyCycle(int(blue  * LED_MAX))
	 
# A function to turn the LedBorg off
def LedOff():
    SetLed(0, 0, 0)
 
# Run until the user presses CTRL+C
print 'Press CTRL+C to exit'
try:
	while True:
		# Loop over a set of different hues:
		for hue in range(30):
		    # Get hue into the 0 to 3 range
		    hue /= 10.0
		    # Decide which two channels we are between
		    if hue < 1.0:
		        # Red to Green
		        red = 1.0 - hue
		        green = hue
		        blue = 0.0
		    elif hue < 2.0:
		        # Green to Blue
		        red = 0.0
		        green = 2.0 - hue
		        blue = hue - 1.0
		    else:
		        # Blue to Red
		        red = hue - 2.0
		        green = 0.
		        blue = 3.0 - hue
		    # Build a list of levels from 1 to 100 to 0
		    levels = range(1, 101)
		    levels2 = range(100)
		    levels2.reverse()
		    levels.extend(levels2)
		    # Loop over the levels
		    for level in levels:
		        # Get level into the 0 to 1 range
		        level /= 100.0
		        # Set the chosen colour and level
		        SetLed(red * level, green * level, blue * level)
		        # Wait a short while
		        time.sleep(pause_time)
		        
except KeyboardInterrupt:  
	RED.ChangeDutyCycle(0)
	GREEN.ChangeDutyCycle(0)
	BLUE.ChangeDutyCycle(0)
	GPIO.cleanup()          # clean up GPIO on CTRL+C exit 
