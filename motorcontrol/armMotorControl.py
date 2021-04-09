import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper


# wheels = MotorKit(i2c = board.I2C(), address = 0x61)
arm = MotorKit(i2c = board.I2C(), address = 0x61)

arm.stepper2.release()

def armUp():
    for i in range(80):
        arm.stepper2.onestep(direction = stepper.BACKWARD, style = stepper.DOUBLE)
        time.sleep(0.0025)
        
def armDown():
    for i in range(90):
        arm.stepper2.onestep(direction = stepper.FORWARD, style = stepper.SINGLE)
        time.sleep(0.005)
        
def openClaw():
    arm.motor2.throttle = 1.0
    time.sleep(0.3)
    arm.motor2.throttle = 0
    
def closeClaw():
    arm.motor2.throttle = -0.75
    time.sleep(0.3)
    arm.motor2.throttle = 0
    
more = 'y'

while more == 'y':
    arm.stepper2.release()
    direction = input('u, d, o, c: ')
    if direction == 'u':
        armUp()
    elif direction == 'd':
        armDown()
    elif direction == 'o':
        openClaw()
    elif direction == 'c':
        closeClaw()
    arm.stepper2.release()
    more = input('y for more: ')
    arm.stepper2.release()


    