import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while True:
	GPIO.wait_for_edge(23, GPIO.FALLING)
	print("Doorbell Pressed!")
	os.system("aplay /home/pi/ring.wav")
	time.sleep(1)
GPIO.clean()
