import time
import board
from adafruit_motorkit import MotorKit

wheels = MotorKit(i2c = board.I2C())


def turnLeft90():
    wheels.motor3.throttle = 0.75
    wheels.motor4.throttle = 0.75
    time.sleep(1)
    wheels.motor3.throttle = 0
    wheels.motor4.throttle = 0
    time.sleep(2)
    
def turnRight90():
    wheels.motor3.throttle = -0.75
    wheels.motor4.throttle = -0.75
    time.sleep(1)
    wheels.motor3.throttle = 0
    wheels.motor4.throttle = 0
    time.sleep(2)
    
def goStraight():
    wheels.motor3.throttle = 0.75
    wheels.motor4.throttle = -0.75
    time.sleep(0.5)
    wheels.motor3.throttle = 0
    wheels.motor4.throttle = 0
    time.sleep(0.5)

def goBack():
    wheels.motor3.throttle = -0.75
    wheels.motor4.throttle = 0.75
    time.sleep(0.5)
    wheels.motor3.throttle = 0
    wheels.motor4.throttle = 0
    time.sleep(0.5)

def turnAround():
    wheels.motor3.throttle = -0.75
    wheels.motor4.throttle = -0.75
    time.sleep(2)
    wheels.motor3.throttle = 0
    wheels.motor4.throttle = 0
    time.sleep(0.5)



# time.sleep(5)
#goStraight()
#goBack()
#turnLeft90()
#turnRight90()
#turnAround()

