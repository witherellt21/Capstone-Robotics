import pygame
from pygame.locals import *
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
#import pyfirmata
import time

'''
#Setup Arduino Board
board = pyfirmata.Arduino('/dev/cu.usbmodemFA131')
it = pyfirmata.util.Iterator(board)
it.start()
X_pin = board.get_pin('a:0:i')
Y_pin = board.get_pin('a:1:i')
'''
'''
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
'''
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


#Vertices
vertices_List = []
vertices_List2 = []
line_vertList = []
bL_vertList = []
lR_vertList = []
lS_vertList = []


#Surfaces
surfaces1 = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )
surfaces2 = (
    (0,1,2,3),
    (0,4,7,3),
    (4,5,6,7),
    (5,1,2,6),
    (0,4,5,1),
    (3,7,6,2)
    )
line_surfaces = (
    (0,1,2,3),
    (0,1,5,4),
    (1,2,6,5),
    (3,2,6,7),
    (3,7,4,0),
    (4,5,6,7),
    )

#car info
pygame.init()
display = (800,600)
screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)


def Draw_Cube(vertices, color, surfaces):
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv(color)
            glVertex3fv(vertices[vertex])
    glEnd()

def Draw_Lines(vertices, color):
    glBegin(GL_QUADS)
    for vertex in line_surface:
        glColor3fv(color)
        glVertex3fv(vertices[vertex])


def drawCar(x,y):
    screen.blit(carImg, (x,y))

def main():
    #pygame.init()
    #display = (800,600)
    #screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #Set clipping planes and perspective degree
    gluPerspective(60.0, (display[0]/display[1]), 6.0, 100.0)

    #Cubes distance from player
    startingX = 0
    startingZ = 5
    glTranslatef(startingX, 0, startingZ)
    moving = ""
    looking = ""
    vision_angle = 0

    #Players location with respect to cube
    glRotatef(0, 0, 0, 0)

    #Running Program
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        pygame.display.flip()
        time.sleep(0.1)
    pygame.quit()

main()