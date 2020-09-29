#import pyfirmata
import time
import pygame
import math
from pygamePieces import Robot, Barrier

pygame.init()
screen = pygame.display.set_mode((1700, 900))

def drawDivider(x, y, Color):
    pygame.draw.rect(screen, Color, (x, y, 10, 900),0)

def barrierExists(barrierList, x, y):
    for barrier in barrierList:
        if barrier.x == x and barrier.y == y:
            return True
    return False



robotX = 800
robotY = 800

robot = Robot(screen, robotX, robotY)

y_change = 0
x_change = 0

barrierList = []

pygame.joystick.init()


running = True
while running:

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYBUTTONDOWN:
            # 0 = A
            # 1 = B
            # 2 = X
            # 3 = Y
            print(event.button)

        if event.type == pygame.JOYHATMOTION:
            if event.value[0] == 1:
                print('hello')
            if event.value[0] == -1:
                print('yo')

    for j in joysticks:
        x_change = j.get_axis(LEFT_X)
        y_change = j.get_axis(LEFT_Y)
        if abs(x_change) <= 0.1:
            x_change = 0
        if abs(y_change) <= 0.1:
            y_change = 0

        #j.get_axis(RIGHT_X)
        #j.get_axis(RIGHT_Y)

    print(y_change)

    robot.y += y_change
    robot.x += x_change

    if x_change > 0:
        pass
        #fl.left()
    if y_change > 0:
        fl.backward()
    elif y_change < 0:
        fl.forward()
    else:
        fl.stop()


    drawDivider(945, 0, (255, 255, 255))
    robot.draw()

    barrierX = 740
    barrierY = 700

    #barrierX = 780
    #barrierY = 600

    if not barrierExists(barrierList, barrierX, barrierY):
        barrier = Barrier(screen, barrierX, barrierY, 5, 5)
        #barrier = Barrier(screen, barrierX, barrierY, 10, 40)
        #barrier = pygame.draw.rect(screen, (255, 255, 255), (780, 600, 40, 10),0)
        barrierList.append(barrier)

    for b in barrierList:
        b.draw()

        robot.displayWarnings(b)
        #if d < 100:
            #robot.getDirection(barrier, d)
        #if isCollision(robot.x, robot.y, barrier.x, barrier.y):
        #    displayWarningUp(robot.x, robot.y)

    pygame.display.update()
    time.sleep(0.001)

pygame.quit()