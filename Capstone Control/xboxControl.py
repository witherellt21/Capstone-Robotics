#!/usr/bin/env python3
'''
Author: Taylor Witherell
Filename: xboxControl.py
Description: Contians Controller class to initialize Xbox controller and receive data
'''

import pygame

class Controller():

    def __init__(self):
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        self.LEFT_X = 0
        self.LEFT_Y = 1
        self.RIGHT_X = 3
        self.RIGHT_Y = 4

    def getAxes(self):

       print(self.joystick.get_axes(0))

if __name__ == '__main__':

   c = Controller()

   while True:

       controller.getAxes()
