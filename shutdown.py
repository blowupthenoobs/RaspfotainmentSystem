
import RPi.GPIO as GPIO
import time
import subprocess

# GPIO / BCM 17 - physical pin 11
PORT = 21

# No. of seconds after ignition returns to cancel shutdown 
CANCEL_SHUTDOWN = 2

IGN_STATUS = 1
SHUTDOWN = 0
IGN_OFF_TIME = 0
IGN_OFF_LAST_SEEN = 0
NOW = 0


# specify pin numbering format
GPIO.setmode(GPIO.BCM)

# set pin to input, set pull up resistor so it reads high
GPIO.setup((PORT), GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
	
	NOW = time.time()

	# Get the status of the ignition
	IGN_UP = GPIO.input(PORT)
 
	# Ignition switched off? then set shutdown flag and igntion off time  
	if IGN_UP and not SHUTDOWN:
		SHUTDOWN = 1
		IGN_OFF_TIME = NOW   

	# Increment this counter while ignition is off 
	if IGN_UP and SHUTDOWN:
		IGN_OFF_LAST_SEEN = NOW 

	# if igntion is off check if shutdown delay time reached
	if (SHUTDOWN and IGN_UP and ((NOW - IGN_OFF_TIME) > SHUTDOWN_DELAY)):
		try:
			STATUS = subprocess.check_output(["shutdown", "-h", "now", "--no-wall"])
		except subprocess.CalledProcessError as shutdowncmd:
			print("Shutdown failed with error code: ", shutdowncmd.returncode)
			break	
	
	# Cancel shutdown if power has been back for CANCEL_SHUTDOWN seconds
	if ((NOW - IGN_OFF_LAST_SEEN) >= CANCEL_SHUTDOWN ) and SHUTDOWN:
		SHUTDOWN = 0
		IGN_OFF_TIME = 0
		IGN_OFF_LAST_SEEN = 0
	time.sleep(1)
  
GPIO.cleanup()
