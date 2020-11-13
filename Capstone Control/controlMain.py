'''
Filename: controlMain.py

Author: Taylor Witherell

Description:  Main running loop for control/operator side of the robot
'''

import time
import pygame
import math
from getData import Receiver
from pygamePieces import Robot, Barrier
from ps3controller import Controller
from PIL import ImageFont

# Toggle simulation elements
server_online = False
pygame_running = True
controller_connected = True
data_status = 'GUI'

# Color List
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
if pygame_running:
    screen = pygame.display.set_mode((1400, 900))

    robotX = 800
    robotY = 800
    robot_angle = 0
    scanner_angle = 0

    robot = Robot(screen, robotX, robotY, 35, 35, (255, 255, 255))
    scanner = Robot(screen, robotX, robotY, 20, 20, (0, 0, 255))

    y_change = 0
    x_change = 0

    barrierList = []

    font = pygame.font.Font('freesansbold.ttf', 32)
    font_24 = pygame.font.Font('freesansbold.ttf', 24) 


# ---------------- Initialize Receiver/Server -----------------
if server_online:
    # Make sure IP and PORT match server side IP and PORT
    IP = '192.168.2.2'
    PORT = 10000
    r = Receiver(IP, PORT)
    r.client.connect()


# ---------------- Initialize Variables -----------------
temp_data = 0
accel_data = ''
gyro_data = ''
sonar_data = 0
ir_data = 1

message = ''


# ---------------- Initialize Controller -----------------
if controller_connected:
    c = Controller()

# Set control mode to either "user-controlled" or "automated
control_mode = "user-controlled"


# ------------------- Configure Robot --------------------

arm_vert_axis = 0
arm_horiz_axis = 0

claw_open = True


# -------------------- Begin Mainloop --------------------
print('Beginning Simulation... \n\n')

elapsedList = []
launch = time.time()

running = True
while running:

    start = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.JOYHATMOTION:
            arm_vert_axis = event.value[1]
            arm_horiz_axis = event.value[0]

    if controller_connected:
        
        # Use start button to quit simulation
        if c.joystick.get_button(9):
            running = False
        
        # Get joystick values for drive control
        scan_axis, x_axis, y_axis = c.get_axes()
        y_axis = - y_axis

        # Get trigger data to control turning
        if c.joystick.get_button(6):
            robot_angle += 2
            scanner_angle += 2
        if c.joystick.get_button(7):
            robot_angle -= 2
            scanner_angle -= 2

        # Set robot to autonomous mode
        if c.joystick.get_button(8):
            time.sleep(0.3)
            if control_mode == "user-controlled":
                control_mode = "autonomous"
            else:
                control_mode = "user-controlled"

        # Control arm movements using D-pad
        if arm_vert_axis:
            if arm_vert_axis > 0:
                print('move arm up')
            else:
                print('move arm down')
        if arm_horiz_axis:
            if arm_horiz_axis > 0:
                print('move arm right')
            else:
                print('move arm left')


        # Pick up item using Triangle button
        if c.joystick.get_button(0):
            if claw_open:
                claw_open = False
                print('\nPick up item\n')
            else:
                print('\nDrop item\n')
                claw_open = True
            time.sleep(0.1)
        
        #print(arm_vert_axis)
            

        # Decrease sensitivity
        if abs(x_axis) < 0.08:
            x_axis = 0
        if abs(y_axis) < 0.08:
            y_axis = 0
        if abs(scan_axis) < 0.08:
            scan_axis = 0

        # Convert angle output to radians
        angle = robot_angle / 180 * math.pi

        # Adjust translational movements based on direction        
        x_change = - y_axis * math.sin(angle)
        y_change = - y_axis * math.cos(angle)

        x_change *= 3
        y_change *= 3

        # Change direction that robot is looking
        scanner_angle -= 2*scan_axis

        # Add controller input to control message
        message += str(y_axis)
        
    
    if server_online:
        
        r.receive()

        data = r.datalist
        
        #GET TEMPERATURE DATA
        #temp_data = r.getTemp(temp_data)

        #GET SONAR DATA
        sonar_data = str(r.getSonar(sonar_data))

        #GET IR PROXIMITY DATA
        ir_data = r.getIR(ir_data)

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
        

    if pygame_running:
        screen.fill(black)
        
        robot.y += y_change
        robot.x += x_change
        scanner.y += y_change
        scanner.x += x_change

        drawDivider(945, 0, (255, 255, 255))
        robot.draw(robot_angle)
        scanner.draw(scanner_angle)

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

        # Display message when in autonomous mode
        if control_mode == "autonomous":
            mode_string = 'Mode: Autonomous'
            displayText(mode_string, font_24, 800, 50)

        if server_online:

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

            # If robot detects an obstacle in close proximity, display message
            if float(sonar_data) < 6 or not ir_data:
                warning_string = 'You are too close to a barrier'
                displayText(warning_string, font, 600, 50)
            
        pygame.display.update()

    if server_online:
        r.client.send(message)
        message = ''

    elapsed = time.time() - start
    elapsedList.append(elapsed)

    if time.time() - launch >= 60:
        running = False
        
    time.sleep(0.001)

total = 0
for time in elapsedList:
    total += time

print('Average Elapsed Time: ', total/len(elapsedList))

pygame.quit()
