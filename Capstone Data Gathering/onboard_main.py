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
server_online = False
trigger_turn = False


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

m1_throttle = 0
m2_throttle = 0

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

    print(msg)

    if server_online:
        # If client disconnects from server, reconnect
        if server.disconnect_counter > 0:
            server.receiveConnection()

        # Send sensor data to client
        server.send(msg)

        # Receive control data from client
        control = server.receive()

        datalist = control.split(',')

        # Wheels are turned at the same ratio as the joystick is held
        # M1 is right side wheel
        # M2 is left side
        if trigger_turn:
            for data in datalist:
                if 'left' in data:
                    m1_throttle = None
                    m2_throttle = -0.8
                elif 'right' in data:
                    m1_throttle = -0.8
                    m2_throttle = None
                elif 'drive' in data:
                    drive = float(data.split('=')[1])
                    m1_throttle = -drive
                    m2_throttle = -drive
        else:
            for data in datalist:
                if 'horiz' in data:
                    turn_factor = float(data.split('=')[1])
                if 'vert' in data:
                    drive = float(data.split('=')[1])

            if turn_factor < 0:
                m1_throttle = -drive - turn_factor
                m2_throttle = -drive
            elif turn_factor > 0:
                m1_throttle = -drive
                m2_throttle = -drive + turn_factor
            else:
                m1_throttle = -drive
                m2_throttle = -drive

        print('Motor 1 Throttle =', m1_throttle, '\nMotor 2 Throttle =', m2_throttle)
        print('')

        if motors_running:

            robot.motor1.throttle = m1_throttle
            robot.motor2.throttle = m2_throttle

    msg = ""

print('done')