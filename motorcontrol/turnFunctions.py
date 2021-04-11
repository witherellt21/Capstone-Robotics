import time
import board
from adafruit_motorkit import MotorKit

wheels = MotorKit(i2c = board.I2C())

class robotManuevers:
    def turnLeft90Over():
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        wheels.motor3.throttle = 0.80
        wheels.motor4.throttle = -0.67
        time.sleep(.84)
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        
    def turnLeft90():
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        wheels.motor3.throttle = 0.7
        wheels.motor4.throttle = -0.65
        time.sleep(.93)
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        
    def turnRight90():
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        wheels.motor3.throttle = -0.68
        wheels.motor4.throttle = 0.67
        time.sleep(.89)
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
        time.sleep(.5)
        
    def goStraight():
        wheels.motor3.throttle = 0.64
        wheels.motor4.throttle = 0.54

#         time.sleep(0.5)
#         wheels.motor3.throttle = 0
#         wheels.motor4.throttle = 0
#         time.sleep(0.5)
    
    def goStraightVeerLeft():
        wheels.motor3.throttle = 0.59
        wheels.motor4.throttle = 0.48
#         time.sleep(0.5)
#         wheels.motor3.throttle = 0
#         wheels.motor4.throttle = 0
#         time.sleep(0.5)

    def goBack():
        wheels.motor3.throttle = -0.75
        wheels.motor4.throttle = -0.75
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
        
    def stopMoving():
        wheels.motor3.throttle = 0
        wheels.motor4.throttle = 0
 
    

# time.sleep(5)
#goStraight()
#goBack()
#turnLeft90()
#turnRight90()
#turnAround()