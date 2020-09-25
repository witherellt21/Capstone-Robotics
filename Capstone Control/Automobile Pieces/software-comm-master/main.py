"""
Author: Nick St. Pierre
Filename: main.py
Description: Program used to simulate the decision algorithm for Mercury Robot.
"""
import pygame, os, random
from modules.vector2D import Vector2
from modules.drawable import Drawable
from modules.obstacle import Obstacle
from modules.robot import Robot


SCREEN_SIZE = Vector2(800, 550)
WORLD_SIZE = Vector2(800, 550)

def main():
   # initialize the pygame module
   pygame.init()
   
   # load and set the logo
   pygame.display.set_caption("Mercury Simulation")
   
   # initialize the screen
   screen = pygame.display.set_mode(list(SCREEN_SIZE))
      
   obstacleList = []
   robot = Robot(Vector2(360,450))
   
   # Let's make a background so we can see if we're moving
   background = Drawable(Vector2(0,0), "background.png", offset = None)
   
   # Initialize the gameClock for more realistic velocity
   gameClock = pygame.time.Clock()
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Draw everything, adjust by offset
      background.draw(screen)
      robot.draw(screen)
      for obstacle in obstacleList:
         obstacle.draw(screen)
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         
         robot.handleEvent(event)
         
         if event.type == pygame.MOUSEBUTTONDOWN:
            adjustedPos = list([int(x) for x in event.pos])
            obstacleList.append(Obstacle(Vector2(*background.adjustMousePos(adjustedPos)), "sidewall.png", SCREEN_SIZE))
            # if event.key == pygame.K_S:
            #     obstacleList.append(Obstacle(Vector2(*background.adjustMousePos(adjustedPos)), "sidewall.png", SCREEN_SIZE))
            # elif event.key == pygame.K_T:
            #     obstacleList.append(Obstacle(Vector2(*background.adjustMousePos(adjustedPos)), "topwall.png", SCREEN_SIZE))
         
      gameClock.tick(60)
      
      ticks = gameClock.get_time() / 1000
            
      
      # Update everything
      robot.update(WORLD_SIZE, ticks)
      for obstacle in obstacleList:         
         if robot.getCollideRect().colliderect(obstacle.getCollideRect()):
            print("You hit the wall")
      
      # Update the camera
      background.updateOffset(robot, SCREEN_SIZE, WORLD_SIZE)
      

   pygame.quit()
   
   
if __name__ == "__main__":
   main()