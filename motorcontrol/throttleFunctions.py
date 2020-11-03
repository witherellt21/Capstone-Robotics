"""
Author: Nick St. Pierre
Filename: throttleFunctions.py
Description: Functions for throttle for the motors
"""

from adafruit_motorkit import MotorKit
import time


def accelerateLinear(motorKit, direction):
    "Increases the throttle"
    
    if direction == "forward":
        motorKit.motor1.throttle = 0.2
        motorKit.motor2.throttle = 0.2
        motorKit.motor3.throttle = 0.2
        motorKit.motor4.throttle = 0.2
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.4
        motorKit.motor2.throttle = 0.4
        motorKit.motor3.throttle = 0.4
        motorKit.motor4.throttle = 0.4
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.6
        motorKit.motor2.throttle = 0.6
        motorKit.motor3.throttle = 0.6
        motorKit.motor4.throttle = 0.6
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.8
        motorKit.motor2.throttle = 0.8
        motorKit.motor3.throttle = 0.8
        motorKit.motor4.throttle = 0.8
        
    elif direction == "backward":
        motorKit.motor1.throttle = -0.2
        motorKit.motor2.throttle = -0.2
        motorKit.motor3.throttle = -0.2
        motorKit.motor4.throttle = -0.2
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.4
        motorKit.motor2.throttle = -0.4
        motorKit.motor3.throttle = -0.4
        motorKit.motor4.throttle = -0.4
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.6
        motorKit.motor2.throttle = -0.6
        motorKit.motor3.throttle = -0.6
        motorKit.motor4.throttle = -0.6
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.8
        motorKit.motor2.throttle = -0.8
        motorKit.motor3.throttle = -0.8
        motorKit.motor4.throttle = -0.8
    
def decelerateLinear(motorKit, direction):
    "Decreases the throttle"
    if direction == "forward":
        motorKit.motor1.throttle = 0.6
        motorKit.motor2.throttle = 0.6
        motorKit.motor3.throttle = 0.6
        motorKit.motor4.throttle = 0.6
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.4
        motorKit.motor2.throttle = 0.4
        motorKit.motor3.throttle = 0.4
        motorKit.motor4.throttle = 0.4
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.2
        motorKit.motor2.throttle = 0.2
        motorKit.motor3.throttle = 0.2
        motorKit.motor4.throttle = 0.2
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.0
        motorKit.motor2.throttle = 0.0
        motorKit.motor3.throttle = 0.0
        motorKit.motor4.throttle = 0.0
        
    elif direction == "backward":
        motorKit.motor1.throttle = -0.6
        motorKit.motor2.throttle = -0.6
        motorKit.motor3.throttle = -0.6
        motorKit.motor4.throttle = -0.6
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.4
        motorKit.motor2.throttle = -0.4
        motorKit.motor3.throttle = -0.4
        motorKit.motor4.throttle = -0.4
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.2
        motorKit.motor2.throttle = -0.2
        motorKit.motor3.throttle = -0.2
        motorKit.motor4.throttle = -0.2
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.0
        motorKit.motor2.throttle = 0.0
        motorKit.motor3.throttle = 0.0
        motorKit.motor4.throttle = 0.0
#---------------------------------------------------    
def accelerateExp(motorKit, direction):
    "Exponential throttle increase"
    """
    if direction == "forward":
        for x in range(interval):
            motorKit.motor1.throttle += x * 0.1
            motorKit.motor2.throttle += x * 0.1
            motorKit.motor3.throttle += x * 0.1
            motorKit.motor4.throttle += x * 0.1
            time.sleep(0.5)
    elif direction == "backward":
        for x in range(interval):
            motorKit.motor1.throttle -= x * 0.1
            motorKit.motor2.throttle -= x * 0.1
            motorKit.motor3.throttle -= x * 0.1
            motorKit.motor4.throttle -= x * 0.1
            time.sleep(0.5)
    """ 
         
       
    if direction == "forward":
        motorKit.motor1.throttle = 0.1
        motorKit.motor2.throttle = 0.1
        motorKit.motor3.throttle = 0.1
        motorKit.motor4.throttle = 0.1
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.2
        motorKit.motor2.throttle = 0.2
        motorKit.motor3.throttle = 0.2
        motorKit.motor4.throttle = 0.2
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.4
        motorKit.motor2.throttle = 0.4
        motorKit.motor3.throttle = 0.4
        motorKit.motor4.throttle = 0.4
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.8
        motorKit.motor2.throttle = 0.8
        motorKit.motor3.throttle = 0.8
        motorKit.motor4.throttle = 0.8
        
    elif direction == "backward":
        motorKit.motor1.throttle = -0.1
        motorKit.motor2.throttle = -0.1
        motorKit.motor3.throttle = -0.1
        motorKit.motor4.throttle = -0.1
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.2
        motorKit.motor2.throttle = -0.2
        motorKit.motor3.throttle = -0.2
        motorKit.motor4.throttle = -0.2
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.4
        motorKit.motor2.throttle = -0.4
        motorKit.motor3.throttle = -0.4
        motorKit.motor4.throttle = -0.4
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.8
        motorKit.motor2.throttle = -0.8
        motorKit.motor3.throttle = -0.8
        motorKit.motor4.throttle = -0.8

    

def decelerateExp(motorKit, direction):
    "Exponential throttle decrease"
    if direction == "forward":
        motorKit.motor1.throttle = 0.6
        motorKit.motor2.throttle = 0.6
        motorKit.motor3.throttle = 0.6
        motorKit.motor4.throttle = 0.6
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.3
        motorKit.motor2.throttle = 0.3
        motorKit.motor3.throttle = 0.3
        motorKit.motor4.throttle = 0.3
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.1
        motorKit.motor2.throttle = 0.1
        motorKit.motor3.throttle = 0.1
        motorKit.motor4.throttle = 0.1
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.0
        motorKit.motor2.throttle = 0.0
        motorKit.motor3.throttle = 0.0
        motorKit.motor4.throttle = 0.0
        
    elif direction == "backward":
        motorKit.motor1.throttle = -0.6
        motorKit.motor2.throttle = -0.6
        motorKit.motor3.throttle = -0.6
        motorKit.motor4.throttle = -0.6
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.3
        motorKit.motor2.throttle = -0.3
        motorKit.motor3.throttle = -0.3
        motorKit.motor4.throttle = -0.3
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.1
        motorKit.motor2.throttle = -0.1
        motorKit.motor3.throttle = -0.1
        motorKit.motor4.throttle = -0.1
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.0
        motorKit.motor2.throttle = 0.0
        motorKit.motor3.throttle = 0.0
        motorKit.motor4.throttle = 0.0
#---------------------------------------------------
        
def accelerateLog(motorKit, direction):
    "Accelerates logarithmically."
    if direction == "forward":
        motorKit.motor1.throttle = 0.1
        motorKit.motor2.throttle = 0.1
        motorKit.motor3.throttle = 0.1
        motorKit.motor4.throttle = 0.1
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.5
        motorKit.motor2.throttle = 0.5
        motorKit.motor3.throttle = 0.5
        motorKit.motor4.throttle = 0.5
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.7
        motorKit.motor2.throttle = 0.7
        motorKit.motor3.throttle = 0.7
        motorKit.motor4.throttle = 0.7
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.8
        motorKit.motor2.throttle = 0.8
        motorKit.motor3.throttle = 0.8
        motorKit.motor4.throttle = 0.8
        
    elif direction == "backward":
        motorKit.motor1.throttle = -0.1
        motorKit.motor2.throttle = -0.1
        motorKit.motor3.throttle = -0.1
        motorKit.motor4.throttle = -0.1
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.5
        motorKit.motor2.throttle = -0.5
        motorKit.motor3.throttle = -0.5
        motorKit.motor4.throttle = -0.5
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.7
        motorKit.motor2.throttle = -0.7
        motorKit.motor3.throttle = -0.7
        motorKit.motor4.throttle = -0.7
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.8
        motorKit.motor2.throttle = -0.8
        motorKit.motor3.throttle = -0.8
        motorKit.motor4.throttle = -0.8        
    
def decelerateLog(motorKit, direction):
    "Deccelerates logarithmically."
    if direction == "forward":
        motorKit.motor1.throttle = 0.6
        motorKit.motor2.throttle = 0.6
        motorKit.motor3.throttle = 0.6
        motorKit.motor4.throttle = 0.6
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.5
        motorKit.motor2.throttle = 0.5
        motorKit.motor3.throttle = 0.5
        motorKit.motor4.throttle = 0.5
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.3
        motorKit.motor2.throttle = 0.3
        motorKit.motor3.throttle = 0.3
        motorKit.motor4.throttle = 0.3
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.0
        motorKit.motor2.throttle = 0.0
        motorKit.motor3.throttle = 0.0
        motorKit.motor4.throttle = 0.0
        
    elif direction == "backward":
        motorKit.motor1.throttle = -0.6
        motorKit.motor2.throttle = -0.6
        motorKit.motor3.throttle = -0.6
        motorKit.motor4.throttle = -0.6
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.5
        motorKit.motor2.throttle = -0.5
        motorKit.motor3.throttle = -0.5
        motorKit.motor4.throttle = -0.5
        time.sleep(0.5)
        motorKit.motor1.throttle = -0.3
        motorKit.motor2.throttle = -0.3
        motorKit.motor3.throttle = -0.3
        motorKit.motor4.throttle = -0.3
        time.sleep(0.5)
        motorKit.motor1.throttle = 0.0
        motorKit.motor2.throttle = 0.0
        motorKit.motor3.throttle = 0.0
        motorKit.motor4.throttle = 0.0
