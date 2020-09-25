'''
Author: Taylor Witherell
Filename: onboard_main.py
Description: Main loop for robot to send and receive data.
'''

from client import Client
from sonar import Sonar
import pygame
import time

# ---------------- Initialize Client -----------------
client = Client()

# Set the client to the server's IP and PORT address
client.IP = '192.168.0.21'
client.PORT = 1234

client.connect()


# ---------------- Initialize Pygame -----------------
pygame.init()
screen = pygame.display.set_mode((600, 600))
msg = 'stop'
counter = 0


# ---------------- Initialize Controller -----------------
joysticks = []
pygame.joystick.init()

for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

print(joysticks)


# ---------------- Initialize Sonar -----------------
s = Sonar(18, 24)

running = True
while running:

    counter += 1

    screen.fill((0,0,0))

    #if counter == 10:
    dist = round(s.distance(), 3)
    time.sleep(.1)
    msg = "sonar = " + str(dist)
    print(msg)
    counter = 0
    client.send(msg)

    pygame.display.update()

    #client.receive()


pygame.quit()