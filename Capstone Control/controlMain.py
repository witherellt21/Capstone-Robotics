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
receiving_data = False
pygame_running = True
controller_connected = True
data_status = 'GUI'

# Color List
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
black = (0, 0, 0)
grey = (200, 200, 200)

# GUI Attributes
height = 700
width = 1300

#sim_height = height/2
#sim_width = height/2
sim_height = height
sim_width = width
sim_x = 0
sim_y = 0
robot_height = robot_width = sim_height * 4/90
scanner_height = scanner_width = sim_height * 2/90

dist_height = sim_height
dist_width = sim_width
dist_x = sim_x
dist_y = sim_y + sim_height


# ---------------- Initialize Pygame -----------------
pygame.init()

def drawDivider():
    pygame.draw.rect(sim_surface, (255,255,255), (sim_width*2/3, sim_y, sim_width/100, sim_height),0)

def barrierExists(barrierList, x, y):
    for barrier in barrierList:
        if barrier.x == x and barrier.y == y:
            return True
    return False

def displayText(surface, text, font, x, y, color, background):
    txt = font.render(text, True, color, background)
    textRect = txt.get_rect()
    center = textRect.width/2
    x -= center
    textRect.center = (x, y)
    surface.blit(txt, textRect)

def drawRobotImage():
    
    pygame.draw.rect(dist_surface, blue, (dist_width/3, \
                                                     dist_height/4, dist_width/3, \
                                                     dist_height/2),0)
    
    #pygame.draw.rect(dist_surface, (150, 150, 150), (15, 20, dist_width/2, dist_height/2),0)


# ---------------- Initialize Pygame Pieces -----------------
if pygame_running:
    
    screen = pygame.display.set_mode((width, height))
    sim_surface = pygame.Surface((sim_width, sim_height))
    dist_surface = pygame.Surface((dist_width, dist_height))

    robotX = sim_width*6/7
    robotY = sim_height* 8/9

    robot_angle = 0
    scanner_angle = 0

    robot = Robot(sim_surface, robotX, robotY, robot_height, robot_width, (255, 255, 255))
    scanner = Robot(sim_surface, robotX, robotY, scanner_height, scanner_width, (0, 0, 255))

    y_change = 0
    x_change = 0

    barrierList = []
    barrier_width = sim_height/100

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
sonar_data = ''
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
controllerList = []
serverList = []
pygameList = []


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

    controller_start = time.time()
    if controller_connected:
        
        # Use start button to quit simulation
        if c.joystick.get_button(9):
            running = False
        
        # Get joystick values for drive control
        scan_axis, x_axis, y_axis = c.get_axes()
        y_axis = - y_axis

        # Get trigger data to control turning
        if c.joystick.get_button(6):
            #robot_angle += 2
            #scanner_angle += 2
            message += "left,"
        if c.joystick.get_button(7):
            #robot_angle -= 2
            #scanner_angle -= 2
            message += "right,"

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
        if abs(x_axis) < 0.11:
            x_axis = 0
        if abs(y_axis) < 0.11:
            y_axis = 0
        if abs(scan_axis) < 0.11:
            scan_axis = 0

        # Add controller input to control message
        message += 'drive = ' + str(y_axis) + ","

    controllerList.append(time.time() - controller_start)

    server_start = time.time()
                          
    if server_online and receiving_data:

        r.receive()
        
        serverList.append(time.time() - server_start)

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
            
    pygame_start = time.time()
    if pygame_running:

        screen.fill(white)
        sim_surface.fill(black)
        dist_surface.fill(grey)


        # Convert angle output to radians
        angle = robot_angle / 180 * math.pi
        
        if controller_connected:
            # Adjust translational movements based on direction        
            x_change = - y_axis * math.sin(angle)
            y_change = - y_axis * math.cos(angle) 

            #x_change *= 3
            #y_change *= 3

            # Change direction that robot is looking
            scanner_angle -= x_axis - 2*scan_axis
            robot_angle -= x_axis
            
        
        robot.y += y_change
        robot.x += x_change
        scanner.y += y_change
        scanner.x += x_change

        #drawDivider()
        robot.draw(robot_angle)
        scanner.draw(scanner_angle)

        barrierX = sim_width * 35/45
        barrierY = sim_height * 2 / 3

        if not barrierExists(barrierList, barrierX, barrierY):
            #barrier = Barrier(screen, barrierX, barrierY, 5, 5)
            barrier = Barrier(sim_surface, barrierX, barrierY, barrier_width, sim_height * 2/45)
            #barrier = pygame.draw.rect(screen, (255, 255, 255), (780, 600, 40, 10),0)
            barrierList.append(barrier)

        for b in barrierList:
            b.draw()
            robot.displayWarnings(b)

        
        # Display message when in autonomous mode
        if control_mode == "autonomous":
            mode_string = 'Mode: Autonomous'
            displayText(sim_surface, mode_string, font_24, width * 4/7, height * 3/18, white, black)

        if server_online and receiving_data:

            if data_status == 'GUI':
                
                ax_string = 'ax = ' + ax
                displayText(sim_surface, ax_string, font, 300, 50, white, black)
                ay_string = 'ay = ' + ay
                displayText(sim_surface, ay_string, font, 300, 130, white, black)
                az_string = 'az = ' + az
                displayText(sim_surface, az_string, font, 300, 210, white, black)
                gx_string = 'gx = ' + gx
                displayText(sim_surface, gx_string, font, 300, 290, white, black)
                gy_string = 'gy = ' + gy
                displayText(sim_surface, gy_string, font, 300, 370, white, black)
                gz_string = 'gz = ' + gz
                displayText(sim_surface, gz_string, font, 300, 450, white, black)
                
                sonar_string = 'dist = ' + sonar_data
                displayText(sim_surface, sonar_string, font, 300, 530, white, black)

                displayText(dist_surface, sonar_data, font_24, dist_width*3/12, dist_height/2, black, grey)
                displayText(dist_surface, sonar_data, font_24, dist_width*11/12, dist_height/2, black, grey)
                displayText(dist_surface, sonar_data, font_24, dist_width*6/10, dist_height/8, black, grey)
                displayText(dist_surface, sonar_data, font_24, dist_width*6/10, dist_height*7/8, black, grey)

            # If robot detects an obstacle in close proximity, display message
            if float(sonar_data) < 6 or not ir_data:
                warning_string = 'You are too close to a barrier'
                displayText(sim_surface, warning_string, font, 900, 50, white, black)
        
        drawRobotImage()

        screen.blit(dist_surface, (dist_x, dist_y))
        screen.blit(sim_surface, (sim_x, sim_y))
        pygame.display.update()
         
    pygameList.append(time.time() - pygame_start)

    if server_online:
        r.client.send(message)

    message = ''

    elapsed = time.time() - start
    elapsedList.append(elapsed)

    if time.time() - launch >= 60:
        pass
        
    time.sleep(0.001)

total = 0
for time in elapsedList:
    total += time

if controller_connected:
    controller_total = 0
    for time in controllerList:
        controller_total += time

    print('Average Elapsed Time for controller code: ', controller_total/len(controllerList))

if server_online:            
    server_total = 0
    for time in serverList:
        server_total += time

    print('Average Elapsed Time for server code: ', server_total/len(serverList))

if pygame_running:
    pygame_total = 0
    for time in pygameList:
        pygame_total += time
    print('Average Elapsed Time for pygame code: ', pygame_total/len(pygameList))
                          
print('Average Elapsed Time: ', total/len(elapsedList))

pygame.quit()
