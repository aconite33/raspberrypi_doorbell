import RPi.GPIO as GPIO
import time
import os


def ring_doorbell():
	os.system("mpg123 /home/pi/clips/Starwars_Intro.mp3")

def debounce(channel):
	#print("Button depressed")
	tries = 12
	i, ones, zeroes = 0, 0, 0
	while i < tries:
		bit=GPIO.input(channel)
		#print("Value of BIT: {:d}".format(bit))
		if (bit == 1):
			ones = ones + 1
			zeroes = 0
		else:
			zeroes = zeroes + 1
			ones = 0
		i = i + 1
		if (ones >= 2):
			ring_doorbell()
			doorbell_Pushed = True
			return 1
		if (zeroes >= 2):
			return 0
			#time.sleep(0.5) # wait a bit
	# indeterminate state, tries exhausted
	#logging.error ('Bouncy input: %s', pin)
	return (bit)   #best effort


doorbell_Pushed = False
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#while True:
GPIO.add_event_detect(23, GPIO.RISING, callback=debounce)

while True:
	#Wait for doorbell
	if(doorbell_Pushed):
		print("Someone pushed the doorbell!")
		GPIO.add_event_detect(23, GPIO.RISING, callback=debounce)
		doorbell_Pushed = False
GPIO.cleanup()
