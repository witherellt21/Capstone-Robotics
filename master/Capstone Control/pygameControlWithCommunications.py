#import pyfirmata
import time
import pygame
import math
from server import Server

pygame.init()
screen = pygame.display.set_mode((1700, 900))

class Barrier():

    def __init__(self, screen, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.screen = screen
        #self.counter = counter

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height),0)


class Robot():

    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.height = 20
        self.width = 20
        self.screen = screen
        self.direction = 'up'

    def draw(self):

        if self.direction == 'up':
            point_of_triangle = (self.x, (self.y - self.height/2))
            coordinates = [(self.x - self.width/2, self.y + self.height/2), point_of_triangle, (self.x + self.width/2, self.y + self.height/2)]
        elif self.direction == 'left':
            point_of_triangle = (self.x - self.width/2, self.y)
            coordinates = [(self.x + self.height/2, self.y - self.width/2), point_of_triangle, (self.x + self.height/2, self.y + self.width/2)]
        elif self.direction == 'right':
            point_of_triangle = (self.x + self.width/2, self.y)
            coordinates = [(self.x - self.height/2, self.y - self.width/2), point_of_triangle, (self.x - self.height/2, self.y + self.width/2)]
        elif self.direction == 'down':
            point_of_triangle = (self.x, (self.y + self.height/2))
            coordinates = [(self.x - self.width/2, self.y - self.height/2), point_of_triangle, (self.x + self.width/2, self.y - self.height/2)]

        #pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height),0)
        pygame.draw.polygon(self.screen, (255, 255, 255), coordinates)

    def getDistance(self, barrier, direction):
        print(direction)
        if direction == 'up' or direction == 'down':
            distance = self.y - barrier.y + barrier.height/2
        elif direction == 'left' or direction == 'right':
            distance = self.x - barrier.x + barrier.width/2
        #distance = math.sqrt(math.pow(self.x - barrier.x + barrier.width/2, 2) + math.pow(self.y - barrier.y + barrier.height/2, 2))
        return distance

    def getDirection(self, barrier):
        #if (self.x + self.width/2 >= barrier.x and self.x + self.width/2 <= barrier.x + barrier.width) or (barrier.x < self.x + self.width/2 and barrier.x + self.width >= self.x - self.width/2):
        if (barrier.x <= self.x + self.width/2 and barrier.x >= self.x - self.width/2) or (barrier.x + barrier.width <= self.x + self.width/2 and barrier.x + barrier.width >= self.x - self.width/2):
            if self.y > barrier.y:
                return 'up'
                #self.displayWarningUp(distance)
            else:
                return 'down'
                #self.displayWarningDown()

        elif self.y >= barrier.y and self.y <= barrier.y + barrier.height:
            if self.x > barrier.x:

                return 'left'
                #self.displayWarningLeft()
            else:

                return 'right'
                #self.displayWarningRight()

    def displayWarningUp(self, distance):
        if distance < 40:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y - 23, 20, 5),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y - 30, 20, 5),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y - 37, 20, 5),0)

        elif distance < 70:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y - 23, 20, 5),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y - 30, 20, 5),0)
        else: pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y - 23, 20, 5),0)

    def displayWarningDown(self, distance):

        if distance < 40:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y + self.height/2 + 10, 20, 5),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y + self.height/2 + 17, 20, 5),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y + self.height/2 + 24, 20, 5),0)

        elif distance < 70:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y + 23, 20, 5),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y + 30, 20, 5),0)
        else: pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2, self.y + 23, 20, 5),0)

    def displayWarningLeft(self, distance):

        if distance < 40:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2 - 10, self.y - self.height/2, 5, 20),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2 - 17, self.y - self.height/2, 5, 20),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2 - 24, self.y - self.height/2, 5, 20),0)

        elif distance < 70:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2 - 10, self.y - self.height/2, 5, 20),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2 - 17, self.y - self.height/2, 5, 20),0)
        else: pygame.draw.rect(self.screen, (255, 0, 0), (self.x - self.width/2 - 10, self.y - self.height/2, 5, 20),0)


    def displayWarningRight(self, distance):
        if distance < 40:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x + self.width/2 + 10, self.y - self.height/2, 5, 20),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x + self.width/2 + 17, self.y - self.height/2, 5, 20),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x + self.width/2 + 24, self.y - self.height/2, 5, 20),0)

        elif distance < 70:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x + self.width/2 + 10, self.y - self.height/2, 5, 20),0)
            pygame.draw.rect(self.screen, (255, 0, 0), (self.x + self.width/2 + 17, self.y - self.height/2, 5, 20),0)
        else: pygame.draw.rect(self.screen, (255, 0, 0), (self.x + self.width/2 + 10, self.y - self.height/2, 5, 20),0)




def drawDivider(x, y, Color):
    pygame.draw.rect(screen, Color, (x, y, 10, 900),0)

'''
def isCollision(robotX, robotY, barrierX, barrierY):
    distance = math.sqrt(math.pow(robotX - barrierX, 2) + math.pow(robotY - barrierY, 2))
    if distance < 100:
        return True
    else:
        return False

def displayWarningUp(x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y - 10, 20, 5),0)
'''
def barrierExists(barrierList, x, y):
    for barrier in barrierList:
        if barrier.x == x and barrier.y == y:
            return True
    return False



robotX = 800
robotY = 800

robot = Robot(screen, robotX, robotY)

y_change = 0
x_change = 0

barrierList = []

IP = "192.168.0.21"
PORT = 1234
s = Server(IP, PORT)
s.start()

running = True
while running:

    screen.fill((0,0,0))

    if s.disconnect_counter == 1:
        s.receiveConnection()

    control = s.receive()

    if control == 'forward':
        robot.direction = 'up'
        y_change = -2
    elif control == 'backward':
        robot.direction = 'down'
        y_change = 2
    elif control == 'left':
        robot.direction = 'left'
        x_change = -2
    elif control == 'right':
        robot.direction = 'right'
        x_change = 2
    elif control == 'stop':
        x_change = 0
        y_change = 0

    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                robot.direction = 'up'
                y_change = -2
            elif event.key == pygame.K_DOWN:
                robot.direction = 'down'
                y_change = 2
            elif event.key == pygame.K_LEFT:
                robot.direction = 'left'
                x_change = -2
            elif event.key == pygame.K_RIGHT:
                robot.direction = 'right'
                x_change = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    '''


    robot.y += y_change
    robot.x += x_change

    drawDivider(945, 0, (255, 255, 255))
    robot.draw()

    barrierX = 740
    barrierY = 700

    #barrierX = 780
    #barrierY = 600

    if not barrierExists(barrierList, barrierX, barrierY):
        barrier = Barrier(screen, barrierX, barrierY, 5, 5)
        #barrier = Barrier(screen, barrierX, barrierY, 10, 40)
        #barrier = pygame.draw.rect(screen, (255, 255, 255), (780, 600, 40, 10),0)
        barrierList.append(barrier)

    for b in barrierList:
        b.draw()

        direction = robot.getDirection(barrier)
        if direction != None:
            distance = robot.getDistance(barrier, direction)
            if distance < 100:
                if direction == 'up':
                    robot.displayWarningUp(distance)
                if direction == 'down':
                    robot.displayWarningDown(distance)
                if direction == 'right':
                    robot.displayWarningRight(distance)
                if direction == 'left':
                    robot.displayWarningLeft(distance)
        #if d < 100:
            #robot.getDirection(barrier, d)
        #if isCollision(robot.x, robot.y, barrier.x, barrier.y):
        #    displayWarningUp(robot.x, robot.y)

    pygame.display.update()
    time.sleep(0.001)

pygame.quit()