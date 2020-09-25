"""
Author: Nick St. Pierre
Filename: drawable.py
Description: A class that contains methods for drawing images to the screen.
"""

import pygame
import os
from .vector2D import Vector2
from .frameManager import FrameManager

class Drawable(object):
    
    WINDOW_OFFSET = Vector2(0,0)
    
    def __init__(self, position, imageName, offset = None):
        self._position = position
        self._imageName = imageName
        self._image = FrameManager.getInstance().getFrame(self._imageName, offset)

    
    @classmethod
    def updateOffset(cls, trackingObject, screenSize, worldSize):
        "This function returns a Vector2 variable containing the offest for drawing to screen"
        cls.WINDOW_OFFSET = Vector2(int(max(0, min(trackingObject.getX() + (trackingObject.getWidth() // 2) - (screenSize[0] // 2), worldSize[0] - screenSize[0]))),
                           int(max(0, min(trackingObject.getY() + (trackingObject.getHeight() // 2) - (screenSize[1] // 2), worldSize[1] - screenSize[1]))))
    
    @classmethod
    def adjustMousePos(cls, mousePos):
        "returns the mouse position adjusted relative to the world position and offset"
        mousePos[0] += cls.WINDOW_OFFSET[0]
        mousePos[1] += cls.WINDOW_OFFSET[1]
        return mousePos

    
    def getPosition(self):
        "returns the position of the drawable"
        return self._position
 
    def setPosition(self, newPosition):
        "sets the position of the drawable to a new position"
        self._position = newPosition
       
    def getSize(self):
        "returns the size of the drawable"
        return self._image.get_size()
 
    def getCollideRect(self):
        "Returns the collision rectangle"
        newRect =  self._position + self._image.get_rect()
        return newRect
    
    def draw(self, surface):
        "Draws the drawable object to a designated surface and adjusts for offset"
        surface.blit(self._image, (self._position[0] - self.WINDOW_OFFSET[0], self._position[1] - self.WINDOW_OFFSET[1]))
      
    def getX(self):
        "Returns the x-position of the orb"
        return self._position[0]
      
    def getY(self):
         "Returns the y-position of the orb"
         return self._position[1]
      
    def getWidth(self):
         "Returns the width of the image"
         return self._image.get_width()
      
    def getHeight(self):
         "Returns the height of the image"
         return self._image.get_height()