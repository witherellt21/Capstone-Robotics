'''
Author: Taylor Witherell
Filename: onboard_main.py
Description: Main loop for robot to send and receive data.
'''

from server import Server
from sonar import Sonar
import pygame
import time
from imu import IMU
from IRsensor import IR
from adafruit_motorkit import MotorKit


sonar_activated = True
imu_activated = True
ir_sensor_activated = True
motors_running = False
server_online = True


# ---------------- Initialize Server -----------------
if server_online:
    # Set the client to the server's IP and PORT address
    IP = '192.168.2.2'
    PORT = 10000
    server = Server(IP, PORT)

    server.start()
    server.receiveConnection()

    print('Connection Received')


# ----------------- Initialize Sonar -----------------
if sonar_activated:
    s = Sonar(18, 24)


# ------------------ Initialize IMU ------------------
if imu_activated:
    imu = IMU()


# ------------------ Initialize IR -------------------
if ir_sensor_activated:
    ir = IR(17)


# ---------------- Initialize Motors -----------------
if motors_running:
    robot = MotorKit()

dist = ''
temp = ''
gyro = ''
acc = ''
ir_status = 1
msg = ''

control = 'stop'
drive = 0
turn_status = "None"

running = True
while running:

    if sonar_activated:
        dist = round(s.distance(), 2)   # Get sonar distance data

        if dist <= 6:
            if motors_running:
                control = 'stop'

    if imu_activated:
        ag_data_ready = imu.driver.read_ag_status().accelerometer_data_available
        if ag_data_ready:
            temp, acc, gyro = imu.read_ag()   # Get IMU data

    if ir_sensor_activated:
        ir_status = ir.status()   # Print status of proximity sensor

    # Compile a data string to send to the client
    msg = "sonar = " + str(dist) + ",, temp = " + str(temp) + ",, accel = " + str(acc) + \
            ",, gyro = " + str(gyro) + ",, ir = " + str(ir_status)

    if server_online:
        # If client disconnects from server, reconnect
        if server.disconnect_counter > 0:
            server.receiveConnection()

        # Send sensor data to client
        server.send(msg)

        # Receive control data from client
        control = server.receive()

        datalist = control.split(',')

        for data in datalist:
            if 'left' in data:
                turn_status = 'left'
            if 'right' in data:
                turn_status = 'right'
            if 'drive' in data:
                drive = float(data.split('=')[1])

        #print(control)

        if motors_running:

            if turn_status == None:
                # Wheels are turned at the same ratio as the joystick is held
                robot.motor1.throttle = -drive # Right side wheels
                robot.motor2.throttle = -drive
                #robot.motor3.throttle = -control # Left side wheels are turned opposite to the right side wheels
                #robot.motor4.throttle = -control

            elif turn_status == 'left':
                robot.motor1.throttle = None # Right side wheels
                robot.motor2.throttle = -0.8

            elif turn_status == 'right':
                robot.motor1.throttle = -0.8 # Right side wheels
                robot.motor2.throttle = 0

        turn_status = None

    msg = ""

print('done')