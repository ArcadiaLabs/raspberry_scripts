#!/usr/bin/env python2.7

from time import sleep
import subprocess
import RPi.GPIO as GPIO

CHANNEL = 18 # GPIO channel 24 is on pin 18 of connector P1
# it will work on any GPIO channel

long_press = 1 #s
very_long_press = 4 #s

GPIO.setmode(GPIO.BOARD) # choose BCM or BOARD numbering schemes. I use BOARD 
GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_UP) # setup the channel as input with a 50K Ohm pull up. A push button will ground the pin, creating a falling edge.

# backlight state
bl_state = 1

def toggle_backlight():
	global bl_state
	if bl_state == 1:
		subprocess.call(['sudo sh -c "echo 1 > /sys/class/backlight/fb_ili9320/bl_power" &'], shell=True)
		bl_state = 0
	else:
		subprocess.call(['sudo sh -c "echo 0 > /sys/class/backlight/fb_ili9320/bl_power" &'], shell=True)
		bl_state = 1

def system_button(CHANNEL):
	button_press_timer = 0
	while True:
			if (GPIO.input(CHANNEL) == False) : # while button is still pressed down
				button_press_timer += 0.1 # keep counting until button is released
			else: # button is released, count for how long
				if (button_press_timer > very_long_press) : # pressed for > 5 seconds
					# do what you want with a very long press
					print "very long press : ", button_press_timer
					subprocess.call(['shutdown -h now "System halted by GPIO action" &'], shell=True)
					
				elif (button_press_timer > long_press) : # press for > 1 < 5 seconds
					# do what you want with a long press
					print "long press : ", button_press_timer
					subprocess.call(['sudo reboot &'], shell=True)
					
				elif (button_press_timer > 0.1):
					# do what you want with a short press
					print "short press : ", button_press_timer					
					# toggle_backlight()

				button_press_timer = 0
			sleep(0.1)

GPIO.add_event_detect(CHANNEL, GPIO.FALLING, callback=system_button, bouncetime=100)
# setup the thread, detect a falling edge on channel and debounce it with 100mSec

# assume this is the main code...
try:
	while True:
		# do whatever while "waiting" for falling edge on channel
		sleep (2)

except KeyboardInterrupt:
	GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
