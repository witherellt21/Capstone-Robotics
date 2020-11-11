#!/usr/bin/env python3

import pygame

class Controller:

    def __init__(self):

        pygame.init()

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

    def run(self):

        while (True):

            # Pump events
            pygame.event.get()

            # Display axis values
            ax = self.my_joystick.get_axis
            print('0:%+3.3f  1:%+3.3f  2:%+3.3f  3:%+3.3f' % (ax(0), ax(1), ax(2), ax(3)))


    def quit(self):
        pygame.display.quit()

if __name__ == '__main__':
   '''
   This will prevent main code being run when someone does from ps3controller import *
   '''
   c = Controller()
   c.run()
