#import pyfirmata
import time
import pygame
import math
from pygamePieces import Robot, Barrier
from xboxControl import Controller
from motor import Motor
from automobile import Automobile

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

c = Controller()
angle = 0
rotation = ''

fl = Motor(4)
##fr = Motor(17)
#br = Motor(22)
#bl = Motor(27)

#robot = Automobile(fr, br, fl, bl)
counter = 0
elapsed_time_list = []

running = True
while running:

    counter += 1

    start_time = time.time()

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYBUTTONDOWN:
            # 0 = A
            # 1 = B
            # 2 = X
            # 3 = Y
            # Left Bumper = 4
            # Right Bumper = 5
            print(event.button)
            if event.button == 4:
                rotation = 'left'
            elif event.button == 5:
                rotation = 'right'
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 4:
                rotation = ''
            elif event.button == 5:
                rotation = ''

        if event.type == pygame.JOYHATMOTION:
            if event.value[0] == 1:
                print('hello')
            if event.value[0] == -1:
                print('yo')

    x_change = c.joystick.get_axis(c.LEFT_X)
    y_change = c.joystick.get_axis(c.LEFT_Y)
    if abs(x_change) <= 0.1:
        x_change = 0
    if abs(y_change) <= 0.1:
        y_change = 0

        #j.get_axis(RIGHT_X)
        #j.get_axis(RIGHT_Y)

    if rotation == 'left':
        angle += 1
    elif rotation == 'right':
        angle -= 1


    robot.y += y_change * math.cos(math.pi*angle/180)
    robot.x += y_change * math.sin(math.pi*angle/180)

    drawDivider(945, 0, (255, 255, 255))
    robot.draw(angle)

    if x_change > 0:
        pass
        #fl.left()
    if y_change > 0:
        fl.backward()
    elif y_change < 0:
        fl.forward()
    else:
        fl.stop()


    barrierX = 740
    barrierY = 700

    #barrierX = 780
    #barrierY = 600

     # making a copy of the old center of the rectangle
    old_center = robot.center
    # defining angle of the rotation
    #rot = (rot + rot_speed) % 360

    # rotating the orignal image
    #new_image = pygame.transform.rotate(robot.surface , rot)
    # set the rotated rectangle to the old center
    #rect.center = old_center
    # drawing the rotated rectangle to the screen
    #screen.blit(new_image , rect)

    '''
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
    '''
    pygame.display.update()

    end_time = time.time()

    elapsed_time = end_time - start_time
    elapsed_time_list.append(elapsed_time)
    total = 0
    if counter == 1000:
        for item in elapsed_time_list:
            total += item
        print(total/counter)
        running = False

    time.sleep(0.001)

pygame.quit()