'''
Author: Taylor Witherell
Filename: onboard_main.py
Description: Main loop for robot to send and receive data.
'''

from client import Client
from sonar import Sonar
import pygame
import time
from imu import IMU
from motor import Motor
from automobile import Automobile


# ---------------- Initialize Client -----------------
server = Server()

# Set the client to the server's IP and PORT address
server.IP = '192.168.0.21'
server.PORT = 1234

server.start()
server.receiveConnection()


# ---------------- Initialize Sonar -----------------
s = Sonar(18, 24)

# ---------------- Initialize IMU -----------------
imu = IMU()
msg = ""

# ---------------- Initialize IR -----------------
ir = IR(14)


'''
# ---------------- Initialize Motors -----------------
fl = Motor()
fr = Motor()
bl = Motor()
br = Motor()

# ---------------- Initialize Automobile -----------------
auto = Automobile(fr, br, fl, bl)
'''

running = True
while running:

    dist = round(s.distance(), 3)

    '''
    if dist <= 6:
        auto.park()
    '''

    ag_data_ready = imu.driver.read_ag_status().accelerometer_data_available
    if ag_data_ready:
        temp, acc, gyro = imu.read_ag()

    print(IR.status)

    time.sleep(.3)

    msg = "sonar = " + str(dist) + ",, temp = " + str(temp) + ",, accel = " + str(acc)+ ",, gyro = " + str(gyro)
    #print(str(msg))

    # If client disconnects from server, reconnect
    if r.server.disconnect_counter > 0:
        r.server.receiveConnection()

    client.send(msg)

    #client.receive()

    msg = ""

print('done')