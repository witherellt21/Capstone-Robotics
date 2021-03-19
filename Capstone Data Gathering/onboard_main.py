'''
Author: Taylor Witherell
Filename: onboard_main.py
Description: Main loop for robot to send and receive data.
'''

from server import Server
from sonar import Sonar
import pygame
import time
from CameraServo import Camera
from armcontrol import Arm
#from imu import IMU
from IRsensor import IR
from adafruit_motorkit import MotorKit
import serial
from usfs import USFS_Master
import math


sonars_activated = True
imu_activated = False
ir_sensor_activated = False
motors_running = True
server_online = True
trigger_turn = False
keyboard_control = False
<<<<<<< HEAD
camera_active = False
cubesensor_active = False
usfs_active = True
camera_active = True
cubesensor_active = False


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
    s_front = Sonar(6, 22)
    s_left = Sonar(5, 23)
    s_right = Sonar(16, 17)
    #s_backright = Sonar(23, 24)
    #s_backleft = Sonar(23, 24)
    print("Sonars")


# ------------------ Initialize IMU ------------------
if imu_activated:
    imu = IMU()


# ------------------ Initialize IR -------------------
if ir_sensor_activated:
    ir = IR(17)


# ---------------- Initialize Motors -----------------
#print("motor1")
if motors_running:
    robot = MotorKit()
    arm = Arm(0x61)
    #print("motor2")
#print("Motor3")

    
# ---------------- Initialize Cube Sensor -----------------
if cubesensor_active:
    ser = serial.Serial(port='/dev/ttyAMA0', baudrate = 9600, timeout=1)
    
    
    
    
    
# ---------------- Initialize USFS -----------------
if usfs_active:
    MAG_RATE = 100
    ACCEL_RATE = 200
    GYRO_RATE = 200
    BARO_RATE = 50
    Q_RATE_DIVISOR = 3
    
    usfs = USFS_Master(MAG_RATE, ACCEL_RATE, GYRO_RATE, BARO_RATE, Q_RATE_DIVISOR)
    
    if not usfs.begin():
        print(usfs.getErrorString())
        exit(1)
        
    usfs.checkEventStatus()
    
    if usfs.gotError():
        print('ERROR: ' + usfs.getErrorString())
        exit(1)
    
    if (usfs.gotQuaternion()):
        
        qw, qx, qy, qz = usfs.readQuaternion()
        
        yaw = math.atan2(2.0 * (qx * qy + qw * qz), qw * qw + qx * qx - qy * qy - qz * qz)
        
        yaw *= 180.0 / math.pi
        yaw += 9.1
        if yaw < 0: yaw += 360.0
        



#ser = serial.Serial(port='/dev/ttyAMA0', baudrate = 9600, timeout=1)


# ---------------- Initialize Camera -----------------
if camera_active:
    c = Camera(18)

dist = ''
temp = ''
gyro = ''
acc = ''
ir_status = 1
msg = ''

arm_status = ''

control = 'stop'
drive = 0
turn_status = "None"

m1_throttle = 0
m2_throttle = 0

distances = []
backleft_dist = '0'
backright_dist = '0'


running = True
while running:

    if server_online:
        
        if server.disconnect_counter > 10:
            server.receiveConnection()

            print('Connection Received')

    if sonars_activated:
        front_dist = round(s_front.distance(), 2)   # Get sonars distance data
        left_dist = round(s_left.distance(), 2)
        right_dist = round(s_right.distance(), 2)
        #backleft_dist = round(s_backleft.distance(), 2)
        #backright_dist = round(s_backright.distance(), 2)
        #if front_dist <= 6:
            #if motors_running:
                #control = 'stop'

        distances = [front_dist, right_dist, backleft_dist, backright_dist, left_dist]

    if imu_activated:
        ag_data_ready = imu.driver.read_ag_status().accelerometer_data_available
        if ag_data_ready:
            temp, acc, gyro = imu.read_ag()   # Get IMU data
    if ir_sensor_activated:
        ir_status = ir.status()   # Print status of proximity sensor

    if cubesensor_active:
        sensor1 = ser.read(1)
        sensor2 = ser.read(1)
        
<<<<<<< HEAD
        print(sensor1, sensor2)
        
        
        
        
        
    if usfs_active:
        pass





=======
>>>>>>> abca825c24e19897306d28fe261a4342759ce725

    if motors_running:
        arm_status = arm.status

    # Compile a data string to send to the client
    msg = "sonar = " + str(distances) + ",, temp = " + str(temp) + ",, accel = " + str(acc) + \
            ",, gyro = " + str(gyro) + ",, ir = " + str(ir_status) + ',,arm =' + str(arm_status) + ',,cube1 =' + str(sensor1) + ',,cube2 =' + str(sensor1) 

    #time.sleep(3)
    if server_online:
        # If client disconnects from server, reconnect
        if server.disconnect_counter > 0:
            server.receiveConnection()
        # Send sensor data to client
        server.send(msg)

        time.sleep(0.03)

        # Receive control data from client
        control = server.receive()

        if control:
            datalist = control.split(',')
            print(datalist)
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
                    if 'm1' in data:
                        try:
                            m1_throttle = round(float(data.split('=')[1]), 2)
                        except:
                            pass
                    elif 'm2' in data:
                        try:
                            m2_throttle = round(float(data.split('=')[1]), 2)
                        except:
                            pass
                    elif data == 'cameraforward':
                        c.FaceForward()
                    elif data == 'camerabackward':
                        c.FaceBackward()
                    elif data == 'cameraleft':
                        c.FaceLeft()
                    elif data == 'cameraright':
                        c.FaceRight()
                    elif data == 'armup':
                        if not arm.status == 'up':
                            arm.armUp()
                            arm.status = 'up'
                    elif data == 'armdown':
                        if not arm.status == 'down':
                            arm.armDown()
                            arm.status = 'down'
                    elif data == 'clawopen':
                        arm.openClaw()
                    elif data == 'clawclosed':
                        arm.closeClaw()
            
        print('Motor 1 Throttle =', m1_throttle, '\nMotor 2 Throttle =', m2_throttle)

        if motors_running:

            robot.motor1.throttle = m1_throttle
            robot.motor2.throttle = m2_throttle
            
        

    msg = ""

print('done')
