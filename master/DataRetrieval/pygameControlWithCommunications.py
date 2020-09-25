#import pyfirmata
import time
import pygame
import math
from getData import Receiver
from pygamePieces import Robot, Barrier

pygame.init()
screen = pygame.display.set_mode((800, 700))

def drawDivider(x, y, Color):
    pygame.draw.rect(screen, Color, (x, y, 10, 900),0)

def barrierExists(barrierList, x, y):
    for barrier in barrierList:
        if barrier.x == x and barrier.y == y:
            return True
    return False

# Initialize Pygame attributes
robotX = 800
robotY = 800

robot = Robot(screen, robotX, robotY)

y_change = 0
x_change = 0

barrierList = []

# Initialize Server/Receiver
IP = "192.168.0.21"
PORT = 1234
r = Receiver(IP, PORT)

# Initialize Sensor values
accel = 0
sonar = 0
imu = 0

running = True
while running:

    screen.fill((0,0,0))

    if r.server.disconnect_counter == 1:
        r.server.receiveConnection()

    r.receive()

    accel = r.getAccel(accel)
    sonar = r.getSonar(sonar)
    imu = r.getIMU(imu)
    
    

    '''

    if control == 'forward':
        robot.direction = 'up'
        y_change = -2
    elif control == 'backward':
        robot.direction = 'down'
        y_change = 2
    elif control == 'left':
        robot.direction = 'left'
        x_change = -2
    elif control == 'right':
        robot.direction = 'right'
        x_change = 2
    elif control == 'stop':
        x_change = 0
        y_change = 0
'''
    
    robot.y += y_change
    robot.x += x_change

    drawDivider(945, 0, (255, 255, 255))
    robot.draw()

    barrierX = 740
    barrierY = 700

    #barrierX = 780
    #barrierY = 600

    if not barrierExists(barrierList, barrierX, barrierY):
        barrier = Barrier(screen, barrierX, barrierY, 10, 10)
        #barrier = Barrier(screen, barrierX, barrierY, 10, 40)
        #barrier = pygame.draw.rect(screen, (255, 255, 255), (780, 600, 40, 10),0)
        barrierList.append(barrier)

    for b in barrierList:
        b.draw()

        direction = robot.getDirection(barrier)
        if direction != None:
            distance = robot.getDistance(barrier, direction)
            if distance < 100:
                if direction == 'up':
                    robot.displayWarningUp(distance)
                if direction == 'down':
                    robot.displayWarningDown(distance)
                if direction == 'right':
                    robot.displayWarningRight(distance)
                if direction == 'left':
                    robot.displayWarningLeft(distance)
        #if d < 100:
            #robot.getDirection(barrier, d)
        #if isCollision(robot.x, robot.y, barrier.x, barrier.y):
        #    displayWarningUp(robot.x, robot.y)
    
    
    pygame.display.update()
    time.sleep(0.001)

pygame.quit()
