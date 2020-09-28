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

# ---------------- Initialize Pygame -----------------
#pygame.init()
#screen = pygame.display.set_mode((600, 600))
msg = 'stop'
counter = 0


# ---------------- Initialize Sonar -----------------
print('start')
s = Sonar(18, 24)
imu = IMU()
msg = []

running = True
while running:

    counter += 1

    #screen.fill((0,0,0))

    #if counter == 10:
    dist = round(s.distance(), 3)

    ag_data_ready = imu.driver.read_ag_status().accelerometer_data_available
    if ag_data_ready:
        temp, acc, gyro = imu.read_ag()

    time.sleep(.1)

    msg.append("sonar = " + str(dist))
    msg.append("temp = " + str(temp))
    msg.append("acc = " + str(acc))
    msg.append("gyro = " + str(gyro))
    print(str(msg))
    #ounter = 0
    client.send(msg)

    #pygame.display.update()

    #client.receive()
    #if counter == 100:
        #running = False

    msg = []

print('done')
#pygame.quit()