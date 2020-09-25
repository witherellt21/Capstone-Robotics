"""
Author: Nick St. Pierre
Filename: motor.py
Description: a motor class uses simple forward backward and stop methods for each servo motor.
"""

import pygame, time
from gpiozero import Servo

class Motor(Servo):

    def __init__ (self, servoPin):
        "Initializes the servo and has basic drive functions"
        self.servo = Servo(servoPin)

    def forward(self):
        "Function that drives the servos forward"
        self.servo.max()
        time.sleep(0.05)

    def backward(self):
        "Function that drives the servos backward"
        self.servo.min()
        time.sleep(0.05)

    def stop(self):
        "Stops motor movement"
        self.servo.detach()



