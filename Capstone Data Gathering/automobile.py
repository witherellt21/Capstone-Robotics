"""
Author: Nick St. Pierre
Filename: automobile.py
Description: File that holds all of the drive and turn functions
"""
from motor import Motor


class Automobile(Motor):
    
    def __init__(self, rightFront, rightRear, leftFront, leftRear):
        self.rightFront = rightFront
        self.rightRear = rightRear
        self.leftFront = leftFront
        self.leftRear = leftRear
        
    def drive(self):
        "Drive all motors forward"
        self.rightFront.forward()
        self.rightRear.forward()
        self.leftFront.forward()
        self.leftRear.forward()
        
    def reverse(self):
        "Drive all motors backward"
        self.rightFront.backward()
        self.rightRear.backward()
        self.leftRear.backward()
        self.leftFront.backward()
        
    def park(self):
        "Stop all motor motion"
        self.rightFront.stop()
        self.rightRear.stop()
        self.leftFront.stop()
        self.leftRear.stop()
        
    def rightTurn(self):
        "Turns right side backward and left side forward to produce a right turn."
        self.rightFront.backward()
        self.rightRear.backward()
        self.leftFront.forward()
        self.leftRear.forward()
        
    def leftTurn(self):
        "Turns left side backward and right side forward to produce a left turn."
        self.rightFront.forward()
        self.rightRear.forward()
        self.leftFront.backward()
        self.leftRear.backward()
        
        
        
    
    