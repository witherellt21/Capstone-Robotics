import pygame
from adafruit_motorkit import MotorKit
import busio
import board
import time
from sonar import Sonar

pygame.init()

kit = MotorKit()
kit.motor3.throttle = 0.0

def turnLeft():
    kit.motor3.throttle = 0.6
    kit.motor4.throttle = -0.6
    time.sleep(1.1)
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    

def turnRight():
    kit.motor3.throttle = -0.6
    kit.motor4.throttle = 0.6
    time.sleep(1.15)
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    
def driveForward():
#     kit.motor3.throttle = 0.5
#     kit.motor4.throttle = 0.45
#     time.sleep(1)
#     kit.motor3.throttle = 0
#     kit.motor4.throttle = 0
    
    kit.motor3.throttle = 1
    kit.motor4.throttle = 1
    time.sleep(4)
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    
    
    
def stop():
    kit.motor3.throttle = 0
    kit.motor4.throttle = 0
    
s_front = Sonar(6, 18)
s_left = Sonar(5, 17)
s_right = Sonar(12, 27)
s_backright = Sonar(13, 22)
s_backleft = Sonar(16, 23)

distances = [1000.0, 1000.0, 1000.0, 1000.0, 1000.0]

front_dist = '0'
backleft_dist = '0'
backright_dist = '0'
left_dist = '0'
right_dist = '0'

turn = ''

turn_prediction = ''

while True:
    '''
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                turnLeft()
    '''
    front_dist = round(s_front.distance(distances[0]), 2)   # Get sonars distance data
    left_dist = round(s_left.distance(distances[4]), 2)
    right_dist = round(s_right.distance(distances[1]), 2)
    backleft_dist = round(s_backleft.distance(distances[2]), 2)
    backright_dist = round(s_backright.distance(distances[3]), 2)
    if front_dist <= 6:
        stop()
    
    distances = [front_dist, right_dist, backleft_dist, backright_dist, left_dist]
    print(distances)
    
        
    if float(left_dist) >= 10:
        turn_prediction = 'left'
    elif float(front_dist) >= 10:
        turn_prediction = 'forward'
    elif float(right_dist) >= 10:
        turn_prediction = 'right'
    else:
        turn_prediction = 'backward'
        
    print('Go ' + turn_prediction)
        
    turn = input('Enter turn:')
    
    
    if turn == 'a':
        turnLeft()
    elif turn == 'd':
        turnRight()
    elif turn == 'w':
        driveForward()
    elif turn == 's':
        stop()
    

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

