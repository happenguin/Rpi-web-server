import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor_ONE_A = 1
Motor_TWO_A = 2
Motor_ONE_B = 3
Motor_TWO_B = 4
Motor_THREE_A = 5
Motor_THREE_B = 6

GPIO.setup(Motor_ONE_A, GPIO.OUT)
GPIO.setup(Motor_ONE_B, GPIO.OUT)
GPIO.setup(Motor_TWO_A, GPIO.OUT)
GPIO.setup(Motor_TWO_B, GPIO.OUT)
GPIO.setup(Motor_THREE_A, GPIO.OUT)
GPIO.setup(Motor_THREE_B, GPIO.OUT)

def forward():
	print "Setting up forward"
	GPIO.output(Motor_ONE_A, GPIO.HIGH)
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	GPIO.output(Motor_TWO_A, GPIO.LOW)
	GPIO.output(Motor_TWO_B, GPIO.HIGH)
	print "Should be moving forward now"
	sleep(2)
	print "Shutting down A and B"
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
	print "Shutting down A and B"
	GPIO.output(Motor_ONE_B, GPIO.LOW)
	GPIO.output(Motor_TWO_A, GPIO.LOW)

def left():
	print "Adjusting to turn"
	GPIO.output(Motor_ONE_A, GPIO.HIGH)
	print "Actually turning"
	sleep(1)
	GPIO.output(Motor_ONE_A, GPIO.LOW)
	print "Setting up left"
	
