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


# ---------------- Initialize Client -----------------
client = Client()

# Set the client to the server's IP and PORT address
client.IP = '192.168.0.21'
client.PORT = 1234

client.connect()


# ---------------- Initialize Sonar -----------------
s = Sonar(18, 24)

# ---------------- Initialize IMU -----------------
imu = IMU()
msg = ""

running = True
while running:

    dist = round(s.distance(), 3)

    ag_data_ready = imu.driver.read_ag_status().accelerometer_data_available
    if ag_data_ready:
        temp, acc, gyro = imu.read_ag()

    time.sleep(.3)

    msg = "sonar = " + str(dist) + ",, temp = " + str(temp) + ",, accel = " + str(acc)+ ",, gyro = " + str(gyro)
    print(str(msg))
    client.send(msg)

    #client.receive()

    msg = ""

print('done')
