'''
Author: Taylor Witherell
Filename: onboard_main.py
Description: Main loop for robot to send and receive data.
'''

from server import Server
from sonar import Sonar
#import pygame
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
motors_running = False
server_online = True
trigger_turn = False
keyboard_control = False
camera_active = False
cubesensor_active = False
usfs_active = False



# ---------------- Initialize Server -----------------
if server_online:
    # Set the client to the server's IP and PORT address
    IP = '192.168.2.2'
    PORT = 20001
    server = Server(IP, PORT)

    server.start()
    server.receiveConnection()

    print('Connection Received')




# ----------------- Initialize Sonar -----------------
if sonars_activated:
    s_backright = Sonar(16, 17)
    s_left = Sonar(5, 23)
    s_right = Sonar(12, 27)
    s_front = Sonar(6, 22)
    s_backleft = Sonar(13, 18)



# ------------------ Initialize IMU ------------------
if imu_activated:
    imu = IMU()



# ------------------ Initialize IR -------------------
if ir_sensor_activated:
    #ir = IR(17)
    pass



# ---------------- Initialize Motors -----------------
#print("motor1")
if motors_running:
    robot = MotorKit()
    arm = Arm(0x61)



# ---------------- Initialize Cube Sensor -----------------
if cubesensor_active:
    ser = serial.Serial(port='/dev/ttyS0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout=1)




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
        
def getYaw():
    
    if (usfs.gotQuaternion()):

            qw, qx, qy, qz = usfs.readQuaternion()

            yaw = math.atan2(2.0 * (qx * qy + qw * qz), qw * qw + qx * qx - qy * qy - qz * qz)

            yaw *= 180.0 / math.pi
            yaw += 9.1
            if yaw < 0: yaw += 360.0
            
            return yaw
        



# ---------------- Initialize Camera -----------------
if camera_active:
    c = Camera(4)

dist = '0'
temp = '0'
gyro = '0'
acc = '0'
ir_status = 1
msg = '0'

yaw = '0'

arm_status = 'up'

control = 'stop'
drive = 0
turn_status = "None"

m1_throttle = 0
m2_throttle = 0

distances = []
front_dist = '0'
backleft_dist = '0'
backright_dist = '0'
left_dist = '0'
right_dist = '0'


#sensor1 = '0'
#sensor2 = '0'


running = True
while running:

    if server_online:

        if server.disconnect_counter > 10:
            server.receiveConnection()

            print('Connection Received')

    if sonars_activated:
        front_dist = s_front.distance()   # Get sonars distance data
        left_dist = s_left.distance()
        right_dist = s_right.distance()
        backleft_dist = s_backleft.distance()
        backright_dist = s_backright.distance()

        distances = [front_dist, right_dist, backleft_dist, backright_dist, left_dist]
        
        for i in range(len(distances)):
            if distances[i] != None:
                distances[i] = round(float(distances[i]),2)

    if imu_activated:
        ag_data_ready = imu.driver.read_ag_status().accelerometer_data_available
        if ag_data_ready:
            temp, acc, gyro = imu.read_ag()   # Get IMU data
    if ir_sensor_activated:
        ir_status = ir.status()   # Print status of proximity sensor

    if cubesensor_active:
        sensor1 = ser.read()
        int_val = int.from_bytes(sensor1, "little", signed = False)
        print(int_val)



    if usfs_active:
        yaw = getYaw()


    if motors_running:
        arm_status = arm.status

    # Compile a data string to send to the client
    msg = "sonar = " + str(distances) + ",, temp = " + str(temp) + ",, accel = " + str(acc) + \
            ",, gyro = " + str(gyro) + ",, ir = " + str(ir_status) + ',,arm =' + str(arm_status) + ',,yaw =' + str(yaw)
    


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
        #print("Controls")
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

        #print('Motor 1 Throttle =', m1_throttle, '\nMotor 2 Throttle =', m2_throttle)

        if motors_running:

            robot.motor1.throttle = m1_throttle
            robot.motor2.throttle = m2_throttle



    msg = ""

print('done')