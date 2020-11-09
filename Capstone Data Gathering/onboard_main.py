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


# ---------------- Initialize Server -----------------

# Set the client to the server's IP and PORT address
try:
    IP = '192.168.0.3'
    PORT = 10000
    server = Server(IP, PORT)
except:
    try:
        IP = '192.168.0.3'
        PORT = 10001
        server = Server(IP, PORT)
    except:
        pass


server.start()
server.receiveConnection()

print('Connection Received')

sonar_status = 'active'
imu_status = 'active'
ir_sensor_status = 'inactive'
motor_status = 'inactive'


# ----------------- Initialize Sonar -----------------
if sonar_status == 'active':
    s = Sonar(18, 24)


# ------------------ Initialize IMU ------------------
if imu_status == 'active':
    imu = IMU()


# ------------------ Initialize IR -------------------
if ir_sensor_status == 'active':
    ir = IR(17)


# ---------------- Initialize Motors -----------------
if motor_status == 'active':
    robot = MotorKit()

dist = ''
temp = ''
gyro = ''
acc = ''
msg = ""

running = True
while running:

    if sonar_status == 'active':
        dist = round(s.distance(), 2)   # Get sonar distance data


        if dist <= 6:
            robot.motor1.throttle = 0 # Right side wheels
            robot.motor2.throttle = 0
            robot.motor3.throttle = 0 # Left side wheels are turned opposite to the right side wheels
            robot.motor4.throttle = 0

    if imu_status == 'active':
        ag_data_ready = imu.driver.read_ag_status().accelerometer_data_available
        if ag_data_ready:
            temp, acc, gyro = imu.read_ag()   # Get IMU data

    if ir_sensor_status == 'active':
        pass
        #print(ir.status())   # Print status of proximity sensor

    # Compile a data string to send to the client
    msg = "sonar = " + str(dist) + ",, temp = " + str(temp) + ",, accel = " + str(acc)+ ",, gyro = " + str(gyro)
    #tag = str(len(msg))
    #msg = tag + msg
    print(str(msg))

    # If client disconnects from server, reconnect
    if server.disconnect_counter > 0:
        server.receiveConnection()

    server.send(msg)
    time.sleep(.3)

    #control = server.receive()

    if motor_status == 'active':
        # Wheels are turned at the same ratio as the joystick is held
        robot.motor1.throttle = control # Right side wheels
        robot.motor2.throttle = control
        robot.motor3.throttle = -control # Left side wheels are turned opposite to the right side wheels
        robot.motor4.throttle = -control


    msg = ""

print('done')
