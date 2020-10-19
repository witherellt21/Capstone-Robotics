
'''
STBY = Pin 13 (GPIO #21)

Motor A:
PWMA = Pin 7 (GPIO #4)
AIN2 = Pin 11 (GPIO #17)
AIN1 = Pin 12 (GPIO #18)

Motor B:
BIN1 = Pin 15 (GPIO #22)
BIN2 = Pin 16 (GPIO #23)
PWMB = Pin 18 (GPIO #24)

'''

# Import required modules
import time
import RPi.GPIO as GPIO

class Motor():

    def __init__(self):

        # Declare the GPIO settings
        GPIO.setmode(GPIO.BOARD)

        self.PWMA = 7
        self.AIN2 = 11
        self.AIN1 = 12
        self.STBY = 13

        # set up GPIO pins
        GPIO.setup(self.PWMA, GPIO.OUT) # Connected to PWMA
        GPIO.setup(self.AIN2, GPIO.OUT) # Connected to AIN2
        GPIO.setup(self.AIN1, GPIO.OUT) # Connected to AIN1
        GPIO.setup(self.STBY, GPIO.OUT) # Connected to STBY

    def forward(self):
        # Drive the motor clockwise
        GPIO.output(self.AIN1, GPIO.HIGH) # Set AIN1
        GPIO.output(self.AIN2, GPIO.LOW) # Set AIN2

        # Set the motor speed
        GPIO.output(self.PWMA, GPIO.HIGH) # Set PWMA

        # Disable STBY (standby)
        GPIO.output(13, GPIO.HIGH)

    def backward(self)
        # Drive the motor counterclockwise
        GPIO.output(self.AIN1, GPIO.LOW) # Set AIN1
        GPIO.output(self.AIN2, GPIO.HIGH) # Set AIN2

        # Set the motor speed
        GPIO.output(self.PWMA, GPIO.HIGH) # Set PWMA

        # Disable STBY (standby)
        GPIO.output(self.STBY, GPIO.HIGH)

    def stop(self):
        # Reset all the GPIO pins by setting them to LOW
        GPIO.output(self.AIN1, GPIO.LOW) # Set AIN1
        GPIO.output(self.AIN2, GPIO.LOW) # Set AIN2
        GPIO.output(self.PWMA, GPIO.LOW) # Set PWMA
        GPIO.output(self.STBY, GPIO.LOW) # Set STBY