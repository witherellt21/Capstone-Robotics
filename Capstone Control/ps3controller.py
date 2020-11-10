#!/usr/bin/env python3

import pygame
from pygame.locals import *

class App:
    def __init__(self):
        pygame.init()

        #pygame.display.set_caption("Joystick Analyzer")

        # Set up the joystick
        pygame.joystick.init()

        self.my_joystick = None
        self.joystick_names = []

        # Enumerate joysticks
        for i in range(0, pygame.joystick.get_count()):
            self.joystick_names.append(pygame.joystick.Joystick(i).get_name())

        # By default, load the first available joystick.
        if (len(self.joystick_names) > 0):
            self.my_joystick = pygame.joystick.Joystick(0)
            self.my_joystick.init()

        max_joy = max(self.my_joystick.get_numaxes(), 
                      self.my_joystick.get_numbuttons(), 
                      self.my_joystick.get_numhats())

        #self.screen = pygame.display.set_mode( (max_joy * 30 + 10, 170) )

        self.font = pygame.font.SysFont("Courier", 20)

    def main(self):

        while (True):

            self.g_keys = pygame.event.get()

            print(self.my_joystick.get_axis(0))

    def quit(self):
        pygame.display.quit()

app = App()
app.main()
