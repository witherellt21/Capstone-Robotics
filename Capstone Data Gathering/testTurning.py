import pygame
from adafruit_motorkit import MotorKit
import busio
import board
import time

pygame.init()

kit = MotorKit()
kit.motor3.throttle = 0.0

def turnLeft():
    kit.motor3.throttle = 1.0
    kit.motor4.throttle = -1.0
    time.sleep(0.6)
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0


while True:
    '''
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                turnLeft()
    '''
    turn = input('Enter turn:')
    
    if turn == 'l':
        turnLeft()


    '''
    Start:

    front thresh = 27
    left thresh = 15
    right thresh = 10

    if left dist > 10:
        get closer (apply throttles to move it slightly left)
    else:
        drive completely straight

    when forced to make first turn (should be right):
    front thresh = 10

    after making a turn the robot should apply the straight method for a few seconds
    '''
