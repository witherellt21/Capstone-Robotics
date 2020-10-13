"""
Author: Nick St. Pierre
Filename: rotateable.py
Description: Contains functions that all for objects to be rotated about their center in pygame.
"""

from .drawable import Drawable
from .vector2D import Vector2

import pygame
import math


class Rotatable(Drawable):
   
   # Debug flag
   DEBUG_DRAW = False
   
   def __init__(self, position,imageName, offset = None):
      super().__init__(position, imageName, offset)

      # Keep track of the actual position so that drawable's draw still works
      self._truePosition = Vector2(*position)
      self._unrotatedImage = self._image
      
      # Rotation angle
      self._angle = 0
      self._pivot = None
      self._center = Vector2(*self._unrotatedImage.get_rect().center) + Vector2(self._position[0], self._position[1])
   
   def setRotated(self):   
      # Calculate degrees because pygame.transform.rotate expects degrees
      degrees = self._angle * 180 / math.pi
      center = self._center

      print(self._truePosition)
      
      self.setPivot((self._position[0],self._position[1]))
      
      # Rotate the surface in its own variable
      rotatedSurface = pygame.transform.rotate(self._unrotatedImage, degrees)
      self._image = rotatedSurface
      
      # Move the relative distance from the rotated surface's offset to find the offset's rotated position on the surface
      #print(self._pivot)
      if self._pivot != None:
         rotatedOffset = self._pivot - self.getRotatedPivot()
      else:
         rotatedOffset = center - Vector2(*rotatedSurface.get_rect().center)

      print(self._truePosition, ",", rotatedOffset)
      # find the new world coordinates based on the old coordinates, moved to the pivot, moved back by the rotated pivot position.   
      newBlit =  rotatedOffset
      #print(newBlit)

      
      self._position = newBlit
      # self._truePosition = self._position
      # return rotatedSurface, newBlit
      
   def getRotatedPivot(self, pivot=None):
      center = self._center
      # Allow for a unique pivot for hinge calculations
      if pivot == None:
         pivot = self._pivot
      #print(center)
      # Obtain a vector representing the relative distance between the center and the pivot
      pivotToCenter = center - pivot

      #print(center, ",", pivot)
      
      # Rotate the relative distance between center and pivot
      pivotToCenterRotated = Vector2(*pivotToCenter)
      #print(pivotToCenterRotated)
      pivotToCenterRotated.rotate(-self._angle)
      print(pivotToCenterRotated)
      
      # Find the new center of the rotated surface
      centerRotated = Vector2(*self._image.get_rect().center)
      #print(centerRotated)
      
      # Move the relative distance from the rotated surface's center to find the pivot's rotated position on the surface
      pivotRotated = centerRotated - pivotToCenterRotated
      #print(pivotRotated)
      
      return pivotRotated
   
   
   def setPivot(self, pivot):
      self._pivot = Vector2(*pivot)
      
   def getPivot(self):
      return self._pivot
   
   def setTruePosition(self, position):
      self._truePosition = Vector2(*position)
   
   def getAngle(self):
      return self._angle
   
   def draw(self, surface):
      # Set image and position to the rotated versions
      #self.setRotated()
      
      super().draw(surface)
      
      # Debugs
      # if Rotatable.DEBUG_DRAW:
      #    pygame.draw.rect(surface, (0,255,0), self._position + self._image.get_rect(), 2)
      #    if self._pivot != None:
      #       pin = self._position + self.getRotatedPivot()
      #    else:
      #       pin = self._position + Vector2(*self._image.get_rect().center)
      #    pygame.draw.circle(surface, (0,255,0), list(map(int, pin)), 6)
         
   def getCenter(self):
      return self._image.get_rect().center

   def increaseAngle(self):
      self._angle += math.pi / 50
      
   def decreaseAngle(self):
      self._angle -= math.pi / 50
   
   # def handleEvent(self, event):
   #    if event.type == pygame.MOUSEMOTION:
   #       mousePos = Vector2(*event.pos)
   #       self._angle = math.atan2(*(mousePos - (self.getPosition() + Vector2(*self.getCenter()))).normalize()) - math.pi / 2
         
      

      
