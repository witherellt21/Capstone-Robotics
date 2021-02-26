'''
Author: Taylor Witherell
Filename: onboard_main.py
Description: Main loop for robot to send and receive data.
'''

from server import Server
from sonar import Sonar
import pygame
import time
#from imu import IMU
from IRsensor import IR
from adafruit_motorkit import MotorKit


sonars_activated = False
imu_activated = False
ir_sensor_activated = False
motors_running = True
server_online = True
trigger_turn = True
keyboard_control = False


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
if sonars_activated:
    print("Sonars1")
    s_front = Sonar(12, 6)
    s_left = Sonar(4, 17)
    s_right = Sonar(27, 22)
    s_back = Sonar(23, 24)
    print("Sonars")


# ------------------ Initialize IMU ------------------
if imu_activated:
    imu = IMU()


# ------------------ Initialize IR -------------------
if ir_sensor_activated:
    ir = IR(17)


# ---------------- Initialize Motors -----------------
print("motor1")
if motors_running:
    robot = MotorKit()
    print("motor2")
print("Motor3")

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

distances = []

running = True
while running:

    if server.disconnect_counter > 10:
        server.receiveConnection()

        print('Connection Received')

    if sonars_activated:
        front_dist = round(s_front.distance(), 2)   # Get sonars distance data
        left_dist = round(s_left.distance(), 2)
        right_dist = round(s_right.distance(), 2)
        back_dist = round(s_back.distance(), 2)
        if front_dist <= 6:
            if motors_running:
                control = 'stop'

        distances = [front_dist, right_dist, back_dist, left_dist]

    if imu_activated:
        ag_data_ready = imu.driver.read_ag_status().accelerometer_data_available
        if ag_data_ready:
            temp, acc, gyro = imu.read_ag()   # Get IMU data
    if ir_sensor_activated:
        ir_status = ir.status()   # Print status of proximity sensor

    # Compile a data string to send to the client
    msg = "sonar = " + str(distances) + ",, temp = " + str(temp) + ",, accel = " + str(acc) + \
            ",, gyro = " + str(gyro) + ",, ir = " + str(ir_status)

    #time.sleep(3)
    if server_online:
        # If client disconnects from server, reconnect
        if server.disconnect_counter > 0:
            server.receiveConnection()
        # Send sensor data to client
        server.send(msg)
        #print('sent')
        time.sleep(0.03)

        # Receive control data from client
        control = server.receive()
        print(control)

        if control:
            datalist = control.split(',')
        # Wheels are turned at the same ratio as the joystick is held
        # M1 is right side wheel
        # M2 is left side
        '''
        if trigger_turn:
            if datalist:
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
                        
        '''
        if keyboard_control:
            for data in datalist:
                if 'forward' in data:
                    m1_throttle = 0.8
                    m2_throttle = 0.8
                elif 'left' in data:
                    m1_throttle = 0.8
                    m2_throttle = None
                if 'right' in data:
                    m1_throttle = None
                    m2_throttle = 0.8
                if 'backward' in data:
                    m1_throttle = -0.8
                    m2_throttle = -0.8
                if 'none' in data:
                    m1_throttle = None
                    m2_throttle = None
        else:
            if datalist:
                for data in datalist:
                    if 'turn' in data:
                        turn_factor = round(float(data.split('=')[1]), 2)
                    if 'mag' in data:
                        mag = round(float(data.split('=')[1]), 2)

                if mag > 0:
                    if turn_factor < 0:
                        m1_throttle = mag
                        m2_throttle = mag + turn_factor
                    elif turn_factor > 0:
                        m1_throttle = mag - turn_factor
                        m2_throttle = mag
                    else:
                        m1_throttle = mag
                        m2_throttle = mag
                elif mag < 0:
                    if turn_factor < 0:
                        m1_throttle = mag
                        m2_throttle = mag - turn_factor
                    elif turn_factor > 0:
                        m1_throttle = mag + turn_factor
                        m2_throttle = mag
                    #elif turn_factor == - 1:
                        #m1_throttle = mag
                        #m2_throttle = - mag
                    #elif turn_factor == 1:
                        #m1_throttle = -mag
                        #m2_throttle = mag
                    else:
                        m1_throttle = mag
                        m2_throttle = mag
                else:
                    m1_throttle = 0
                    m2_throttle = 0
                    
            if trigger_turn:
                if datalist:
                    if 'triggerleft' in datalist:
                        m1_throttle = mag
                        m2_throttle = -mag
                    if 'triggerright' in datalist:
                        m1_throttle = -mag
                        m2_throttle = mag
                    
            


        #print('Motor 1 Throttle =', m1_throttle, '\nMotor 2 Throttle =', m2_throttle)
        #print('')
        #print('')

        if motors_running:

            robot.motor1.throttle = m1_throttle
            robot.motor2.throttle = m2_throttle

    msg = ""

print('done')
