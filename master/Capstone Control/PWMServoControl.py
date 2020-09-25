import RPi.GPIO as GPIO


def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(17, True)
    pwm.ChangeDutyCycle(duty)
    GPIO.output(17, False)
    pwm.ChangeDutyCycle(0)

servoPin = 18
GPIO.setmode(GPIO.BOARD)

GPIO.setup(servoPin, GPIO.OUT)

servo = GPIO.PWM(servoPin, 50) # GPIO 17 for PWM with 50Hz
servo.start(2.5)
setAngle(90)

