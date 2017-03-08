import RPi.GPIO as GPIO
from time import sleep


Motor_ONE_A = 1
Motor_TWO_A = 2
Motor_ONE_B = 3
Motor_TWO_B = 4
Motor_THREE_A = 5
Motor_THREE_B = 6


def forward():
	print "Setting up forward"
	GPIO.output(Motor_ONE_A, GPIO.HIGH)
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	GPIO.output(Motor_TWO_A, GPIO.LOW)
	GPIO.output(Motor_TWO_B, GPIO.HIGH)
	print "Should be moving forward now"
	sleep(2)
	print "Shutting down ONE AND TWO"
	GPIO.output(Motor_ONE_A, GPIO.LOW)
	GPIO.output(Motor_TWO_B, GPIO.LOW)

def backward():
	print "Setting up backward"
	GPIO.output(Motor_ONE_A, GPIO.LOW)
	GPIO.output(Motor_ONE_B, GPIO.HIGH)
	GPIO.output(Motor_TWO_A, GPIO.HIGH)
	GPIO.output(Motor_TWO_B, GPIO.LOW)
	print "Should be moving backward now"
	sleep(2)
	print "Shutting down ONE and TWO"
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	GPIO.output(Motor_TWO_A, GPIO.LOW)

def left():
	print "Adjusting to turn"
	GPIO.output(Motor_ONE_A, GPIO.HIGH)
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	print "Actually turning"
	sleep(1)
	GPIO.output(Motor_ONE_A, GPIO.LOW)
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	print "Setting up left"
	GPIO.output(Motor_THREE_A, GPIO.HIGH)
	GPIO.output(Motor_THREE_B, GPIO.LOW)
	GPIO.output(Motor_TWO_A, GPIO.LOW)
	GPIO.output(Motor_TWO_B, GPIO.HIGH)
	print "Should be moving forward now"
	sleep(2)
	print "Shutting down TWO AND THREE"
	GPIO.output(Motor_THREE_A, GPIO.LOW)
	GPIO.output(Motor_TWO_B, GPIO.LOW)
	print "Readjusting to turn"
	GPIO.output(Motor_ONE_B, GPIO.HIGH)
	GPIO.output(Motor_ONE_A, GPIO.LOW)
	sleep(1)
	GPIO.output(Motor_ONE_B, GPIO.LOW)

def right():
	print "Adjusting to turn"
	GPIO.output(Motor_ONE_B, GPIO.HIGH)
	GPIO.output(Motor_ONE_A, GPIO.LOW)
	print "Actually turning"
	sleep(1)
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	print "Setting up left"
	GPIO.output(Motor_THREE_A, GPIO.HIGH)
	GPIO.output(Motor_THREE_B, GPIO.LOW)
	GPIO.output(Motor_TWO_A, GPIO.LOW)
	GPIO.output(Motor_TWO_B, GPIO.HIGH)
	print "Should be moving forward now"
	sleep(2)
	print "Shutting down TWO AND THREE"
	GPIO.output(Motor_THREE_A, GPIO.LOW)
	GPIO.output(Motor_TWO_B, GPIO.LOW)
	print "Readjusting to turn"
	GPIO.output(Motor_ONE_A, GPIO.HIGH)
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	sleep(1)
	GPIO.output(Motor_ONE_A, GPIO.LOW)

def clockwise():
	print "Staring to turn"
	GPIO.output(Motor_ONE_A, GPIO.HIGH)
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	GPIO.output(Motor_TWO_A, GPIO.HIGH)
	GPIO.output(Motor_TWO_B, GPIO.LOW)
	GPIO.output(Motor_THREE_A, GPIO.HIGH)
	GPIO.output(Motor_THREE_B, GPIO.LOW)
	print "Lets turn ClockWise"
	sleep(2)
	print "Turning off clockwise"
	GPIO.output(Motor_THREE_A, GPIO.LOW)
	GPIO.output(Motor_ONE_A, GPIO.LOW)
	GPIO.output(Motor_TWO_A, GPIO.LOW)

def counterClockwise():
	print "Staring to turn"
	GPIO.output(Motor_ONE_A, GPIO.LOW)
	GPIO.output(Motor_ONE_B, GPIO.HIGH)
	GPIO.output(Motor_TWO_A, GPIO.LOW)
	GPIO.output(Motor_TWO_B, GPIO.HIGH)
	GPIO.output(Motor_THREE_A, GPIO.LOW)
	GPIO.output(Motor_THREE_B, GPIO.HIGH)
	print "Lets turn CounterClockWise"
	sleep(2)
	print "Turning off counterclockwise"
	GPIO.output(Motor_THREE_B, GPIO.LOW)
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	GPIO.output(Motor_TWO_B, GPIO.LOW)

def execute(queue):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Motor_ONE_A, GPIO.OUT)
	GPIO.setup(Motor_ONE_B, GPIO.OUT)
	GPIO.setup(Motor_TWO_A, GPIO.OUT)
	GPIO.setup(Motor_TWO_B, GPIO.OUT)
	GPIO.setup(Motor_THREE_A, GPIO.OUT)
	GPIO.setup(Motor_THREE_B, GPIO.OUT)

	for item in queue:
		if(item == "Up"):
			forward()
		elif(item == "Down"):
			backward()
		elif(item == "Left"):
			left()
		elif(item == "Right"):
			right()
		elif(item == "CW"):
			clockwise()
		elif(item == "CCW"):
			counterClockwise()

	shutdown()


def shutdown():
	GPIO.cleanup()
