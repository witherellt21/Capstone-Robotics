"""
Author: Nick St. Pierre
Filename: obstacle.py
Description: A class that contains obstacle methods for testing robot decisions.
"""

import pygame, os, random
from .drawable import Drawable
from .vector2D import Vector2
from .frameManager import FrameManager

class Obstacle(Drawable):
   
      def __init__(self, position, imageName, screenSize):
         "Initializes the position of the orb to the middle of the world"
         super().__init__(position, imageName, offset = None)
         self._position = position
         
      # def update(self, worldInfo, ticks):
      #   "Updates the obstacle's position based on its current velocity"
      #   self._position = 