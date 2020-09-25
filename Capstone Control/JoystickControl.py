'''
Author: Taylor Witherell
File: JoystickControl.py
Description: Takes input from joystick and converts to an onscreen movement of the robot simulation
'''

import pygame
from pygame.locals import *
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pyfirmata
import time

#Setup Arduino Board
board = pyfirmata.Arduino('/dev/cu.usbmodemFA131')
it = pyfirmata.util.Iterator(board)
it.start()
X_pin = board.get_pin('a:0:i')
Y_pin = board.get_pin('a:1:i')

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    )

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
    )

vertices_List = []
light = (1, 2, 3)

for i in range(0,20):
    vertices6 = (
        (6, -9, -10-2*i),
        (6, -7, -10-2*i),
        (0, -7, -10-2*i),
        (0, -9, -10-2*i),
        (6, -9, -12-2*i),
        (6, -7, -12-2*i),
        (0, -9, -12-2*i),
        (0, -7, -12-2*i),
        )
    vertices_List.append(vertices6)

def Draw_Cube():
    glBegin(GL_QUADS)
    for j in range(len(vertices_List)):
        vertices7 = vertices_List[j]

        for surface in surfaces:
            x = 0

            for vertex in surface:
                x+=1
                glColor3fv(colors[x])
                glVertex3fv(vertices7[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        y = 0
        for vertex in surface:
            y+=1
            glColor3fv(colors[y])
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #Set clipping planes and perspective degree
    gluPerspective(45.0, (display[0]/display[1]), 6.0, 50.0)

    #Cubes distance from player
    startingX = 0
    startingZ = 0
    glTranslatef(startingX, 0, startingZ)
    moving = ""
    looking = ""
    vision_angle = 0

    #Players location with respect to cube
    glRotatef(0, 0, 0, 0)

    #Running Program
    running = True
    while running:
        startingX = 0
        startingZ = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #print(Y_pin.read())
        if X_pin.read == None:
            X_val = 0
            Y_val = 0
        if Y_pin.read() == None:
            Y_val = 0
            x_val = 0
        else:
            X_val = (0.4858 - X_pin.read())
            Y_val = (0.4976 - Y_pin.read())

        #print(Y_val)
        startingZ += Y_val
        startingX += X_val


        #glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Draw_Cube()
        glTranslate(startingX, 0, startingZ)
        pygame.display.flip()
        time.sleep(0.1)
    pygame.quit()

main()