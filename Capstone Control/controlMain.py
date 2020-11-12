'''
Filename: controlMain.py

Author: Taylor Witherell

'''

import time
import pygame
import math
from getData import Receiver
from pygamePieces import Robot, Barrier
from ps3controller import Controller
from PIL import ImageFont


server_status = "active"
pygame_status = "active"
controller_status = "active"
data_status = 'None'

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
black = (0, 0, 0)

# ---------------- Initialize Pygame -----------------
pygame.init()

def drawDivider(x, y, Color):
    pygame.draw.rect(screen, Color, (x, y, 10, 900),0)

def barrierExists(barrierList, x, y):
    for barrier in barrierList:
        if barrier.x == x and barrier.y == y:
            return True
    return False

def displayText(text, font, x, y):
    txt = font.render(text, True, white, black)
    textRect = txt.get_rect()
    center = textRect.width/2
    x -= center
    textRect.center = (x, y)
    screen.blit(txt, textRect)
    


# ---------------- Initialize Pygame Pieces -----------------
if pygame_status == "active":
    screen = pygame.display.set_mode((1400, 900))

    robotX = 800
    robotY = 800
    robot_angle = 0

    robot = Robot(screen, robotX, robotY)

    y_change = 0
    x_change = 0

    barrierList = []

    font = pygame.font.Font('freesansbold.ttf', 32) 


# ---------------- Initialize Receiver/Server -----------------
if server_status == "active":

    IP = '192.168.2.2'
    PORT = 10000
    r = Receiver(IP, PORT)
    r.client.connect()


# ---------------- Initialize Variables -----------------
temp_data = 0
accel_data = ''
gyro_data = ''
sonar_data = 0

message = ''

if controller_status == "active":
    c = Controller()

print('Beginning Simulation... \n\n')

# ---------------- Begin Mainloop -----------------
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYHATMOTION:
            if event.value[0] == 1:
                print('hello')
            if event.value[0] == -1:
                print('yo')

    if controller_status == "active":
        x_axis, y_axis = c.get_axes()

        y_axis = - y_axis

        if abs(x_axis) < 0.08:
            x_axis = 0
        if abs(y_axis) < 0.08:
            y_axis = 0

        if c.joystick.get_button(6):
            robot_angle += 2
        if c.joystick.get_button(7):
            robot_angle -= 2

        angle = robot_angle / 180 * math.pi
        
        x_change = - y_axis * math.sin(angle)
        y_change = - y_axis * math.cos(angle)

        x_change *= 3
        y_change *= 3

    
    if server_status == "active":
        
        r.receive()

        data = r.datalist
        
        #GET TEMPERATURE DATA
        #temp_data = r.getTemp(temp_data)

        #GET ACCELEROMETER DATA
        accel_data = r.getAccel(accel_data)
        a_datalist = accel_data.split(',')
        ax = a_datalist[0].strip('[')
        ay = a_datalist[1]
        az = a_datalist[2].strip(']')

        #GET GYROSCOPE DATA
        gyro_data = r.getGyro(gyro_data)
        g_datalist = gyro_data.split(',')
        gx = g_datalist[0].strip('[')
        gy = g_datalist[1]
        gz = g_datalist[2].strip(']')
        
        if 'sonar' in g_datalist[2]:
            gz = g_datalist[2].strip(']sonar')
        else: gz = g_datalist[2].strip(']')

        #GET SONAR DATA
        sonar_data = str(r.getSonar(sonar_data))

        if data_status == 'printing':
            print('\n')
            print('ax =', ax)
            print('ay =', ay)
            print('az =', az)

            print('\n')
            print('gx =', gx)
            print('gy =', gy)
            print('gz =', gz)
            
            print('\n')
            print('temp = ', temp_data)
            print('sonar = ', sonar_data)
        

    if pygame_status == "active":
        screen.fill(black)
        
        robot.y += y_change
        robot.x += x_change

        drawDivider(945, 0, (255, 255, 255))
        robot.draw(robot_angle)

        barrierX = 740
        barrierY = 700

        if not barrierExists(barrierList, barrierX, barrierY):
            #barrier = Barrier(screen, barrierX, barrierY, 5, 5)
            barrier = Barrier(screen, barrierX, barrierY, 10, 40)
            #barrier = pygame.draw.rect(screen, (255, 255, 255), (780, 600, 40, 10),0)
            barrierList.append(barrier)

        for b in barrierList:
            b.draw()
            robot.displayWarnings(b)

        if server_status == 'active':

            if data_status == 'GUI':
                ax_string = 'ax = ' + ax
                displayText(ax_string, font, 1230, 50)
                ay_string = 'ay = ' + ay
                displayText(ay_string, font, 1230, 130)
                az_string = 'az = ' + az
                displayText(az_string, font, 1230, 210)
                gx_string = 'gx = ' + gx
                displayText(gx_string, font, 1230, 290)
                gy_string = 'gy = ' + gy
                displayText(gy_string, font, 1230, 370)
                gz_string = 'gz = ' + gz
                displayText(gz_string, font, 1230, 450)
                
                sonar_string = 'dist = ' + sonar_data
                displayText(sonar_string, font, 1230, 530)

            if float(sonar_data) < 6:
                warning_string = 'You are too close to a barrier'
                displayText(warning_string, font, 600, 50)
                


    #r.client.send(message)
    
    pygame.display.update()
    time.sleep(0.001)

pygame.quit()
