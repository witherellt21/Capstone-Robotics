#import pyfirmata
import time
import pygame
import math
from getData import Receiver
from pygamePieces import Robot, Barrier
from xboxControl import Controller

# ---------------- Initialize Pygame -----------------
pygame.init()
screen = pygame.display.set_mode((600, 600))

def drawDivider(x, y, Color):
    pygame.draw.rect(screen, Color, (x, y, 10, 900),0)

def barrierExists(barrierList, x, y):
    for barrier in barrierList:
        if barrier.x == x and barrier.y == y:
            return True
    return False


# ---------------- Initialize Pygame Pieces -----------------
robotX = 800
robotY = 800

robot = Robot(screen, robotX, robotY)

y_change = 0
x_change = 0

barrierList = []


# ---------------- Initialize Receiver/Server -----------------
IP = '192.168.0.21'
PORT = 1234
r = Receiver(IP, PORT)


# ---------------- Initialize Variables -----------------
temp_data = 0
accel_data = ''
gyro_data = ''
sonar_data = 0

c = Controller()


# ---------------- Begin Mainloop -----------------
running = True
while running:

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

        print(j.get_axis(RIGHT_X))
        print(j.get_axis(RIGHT_Y))

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
    screen.fill((0,0,0))

    if r.server.disconnect_counter > 0:
        r.server.receiveConnection()

    r.receive()

    data = r.datalist


    #GET TEMPERATURE DATA
    temp_data = r.getTemp(temp_data)

    #GET ACCELEROMETER DATA
    accel_data = r.getAccel(accel_data)
    a_datalist = accel_data.split(',')
    ax = a_datalist[0].strip('[')
    ay = a_datalist[1]
    az = a_datalist[2].strip(']')

    print('\n')
    print('ax =', ax)
    print('ay =', ay)
    print('az =', az)

    #GET GYROSCOPE DATA
    gyro_data = r.getGyro(gyro_data)
    g_datalist = gyro_data.split(',')
    gx = g_datalist[0].strip('[')
    gy = g_datalist[1]
    if 'sonar' in g_datalist[2]:
        gz = g_datalist[2].strip(']sonar')
    else: gz = g_datalist[2].strip(']')

    print('\n')
    print('gx =', gx)
    print('gy =', gy)
    print('gz =', gz)

    #GET SONAR DATA
    sonar_data = r.getSonar(sonar_data)

    print('\n')
    print('temp = ', temp_data)
    print('sonar = ', sonar_data)

    time.sleep(.1)



    '''

    if control == 'forward':
        robot.direction = 'up'
        bl.forward()
        y_change = -2

    elif control == 'backward':
        robot.direction = 'down'
        bl.backward()
        y_change = 2

    elif control == 'left':
        robot.direction = 'left'
        x_change = -2

    elif control == 'right':
        robot.direction = 'right'
        x_change = 2

    elif control == 'stop':
        auto.park()
        y_change = 0
        x_change = 0
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