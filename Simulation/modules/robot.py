"""
Author: Nick St. Pierre
Filename: robot.py
Description: representation of the robot in the simulation.
Will be guided by the decision algorithm.
"""

import pygame, os, random
from .rotatable import Rotatable
from .vector2D import Vector2

class Robot(Rotatable):
    
    def __init__(self, position):
        super().__init__(position, "robot.png", offset = None)
        self._velocity = Vector2(0,0)
        # need to adjust these velocities for realistic numbers
        self._maxVelocity = 50
        self._acceleration = 5
        self._angularAccel = 1
        self._movement = {pygame.K_UP: False,
                 pygame.K_DOWN: False,
                 pygame.K_RIGHT: False,
                 pygame.K_LEFT: False,
                 pygame.K_SPACE: False}
        # self._proximity = pygame.Rect(100,100,100,100)
        
    def getCollideRect(self):
        "Returns the collision rectangle"
        newRect =  self._position + self._image.get_rect()
        return newRect
    
    # def sensor(self, ticks):
    #     self.getCollideRect()
    #     newPosition = self._position + self._velocity * ticks
        
    def handleEvent(self, event):
        "Listens to the event and changes the state of the arrow keys in the _movement"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self._movement[pygame.K_DOWN] = True
            elif event.key == pygame.K_UP:
                self._movement[pygame.K_UP] = True
            elif event.key == pygame.K_LEFT:
                self._movement[pygame.K_LEFT] = True
            elif event.key == pygame.K_RIGHT:
                self._movement[pygame.K_RIGHT] = True
            elif event.key == pygame.K_SPACE:
                self._movement[pygame.K_SPACE] = True
      
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self._movement[pygame.K_DOWN] = False
                self._velocity[1] = 0
            elif event.key == pygame.K_UP:
                self._movement[pygame.K_UP] = False
                self._velocity[1] = 0
            elif event.key == pygame.K_LEFT:
                self._movement[pygame.K_LEFT] = False
                self._velocity[0] = 0
            elif event.key == pygame.K_RIGHT:
                self._movement[pygame.K_RIGHT] = False
                self._velocity[0] = 0
            elif event.key == pygame.K_SPACE:
                self._movement[pygame.K_SPACE] = False
    
    def update(self, worldInfo, ticks):
        "Updates the star's position based on its current velocity"
        # this acceleratees the star in the given arrow key direction
        if self._movement[pygame.K_UP]:
            self._velocity[1] += -self._acceleration
        elif self._movement[pygame.K_DOWN]:
            self._velocity[1] += self._acceleration
        elif self._movement[pygame.K_RIGHT]:
            # self._velocity[0] += self._acceleration
            self.decreaseAngle()
        elif self._movement[pygame.K_LEFT]:
            # self._velocity[0] += -self._acceleration
            self.increaseAngle()
            self.setRotated()
        elif self._movement[pygame.K_SPACE]:
            self._velocity[0], self._velocity[1] = 0, 0

        # This code is the logic behind the bouncing star
        newPosition = self._position + self._velocity * ticks
        if newPosition[0] < 0:
            # exit left
            self._velocity[0] = 0
        elif newPosition[1] < 0:
            # exit top
            self._velocity[1] = 0
        elif newPosition[0] + self.getWidth() > worldInfo[0]:
            # exit right
            self._velocity[0] = 0
        elif newPosition[1] + self.getHeight() > worldInfo[1]:
            # exit bottom
            self._velocity[1] = 0
        

        # a check to make sure the velocity does not exceed the maxVelocity 
        if self._velocity.magnitude() > self._maxVelocity:
            self._velocity.scale(self._maxVelocity)
        #self._position += self._velocity * ticks
        #print(self._position)
        self.setTruePosition(self._position)
    
    # def increaseVelocity(self, index):
    #     "Function used to incrementally increase velocity"
    #     self._velocity[index] += self._acceleration
    # 
    # def decreaseVelocity(self, index):
    #     "Function used to incrementally decrease velocity"
    #     self._velocity[index] -= self._acceleration
