import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper


wheels = MotorKit(i2c = board.I2C(), address = 0x61)
arm = MotorKit(i2c = board.I2C(), address = 0x61)

arm.stepper1.release()

def armUp():
    for i in range(80):
        arm.stepper1.onestep(direction = stepper.BACKWARD, style = stepper.SINGLE)
        time.sleep(0.005)
        
def armDown():
    for i in range(90):
        arm.stepper1.onestep(direction = stepper.FORWARD, style = stepper.SINGLE)
        time.sleep(0.005)
        
def openClaw():
    arm.motor3.throttle = 1.0
    time.sleep(0.3)
    arm.motor3.throttle = 0
    
def closeClaw():
    arm.motor3.throttle = -0.75
    time.sleep(0.3)
    arm.motor3.throttle = 0
    
more = 'y'

while more == 'y':
    arm.stepper1.release()
    direction = input('u, d, o, c: ')
    if direction == 'u':
        armUp()
    elif direction == 'd':
        armDown()
    elif direction == 'o':
        openClaw()
    elif direction == 'c':
        closeClaw()
    arm.stepper1.release()
    more = input('y for more: ')
    arm.stepper1.release()


    