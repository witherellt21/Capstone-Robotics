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