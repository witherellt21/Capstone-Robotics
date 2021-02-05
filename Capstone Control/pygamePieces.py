import math
import pygame

class Robot():

    def __init__(self, screen, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.screen = screen
        self.center = (self.x, self.y)
        self.surface = pygame.Surface((self.width, self.height))
        self.angle = 0
        self._direction = 'up'

        #For automation:
        self.firstMove = 'left'
        self.secondMove = 'up'
        self.thirdMove = 'right'
        self.fourthMove = 'down'

    def draw(self):

        angle = math.pi*self.angle/180
        
        point_of_triangle = (self.x + self.height/2 * math.cos(math.pi*90/180 + angle), (self.y - self.height/2 * math.sin(math.pi*90/180 + angle)))
        bottom_left = (self.x + self.height/2 * math.cos(math.pi*225/180 + angle), self.y - self.height/2 * math.sin(math.pi*225/180 + angle))
        bottom_right = (self.x + self.height/2 * math.cos(math.pi*315/180 + angle), self.y - self.height/2 * math.sin(math.pi*315/180 + angle))
        coordinates = [bottom_left, point_of_triangle, bottom_right]
    
        pygame.draw.polygon(self.screen, self.color, coordinates)

    #Gets distance of adjacent barrier from direction
    def getDistance(self, barrier, direction):
        if direction == 'up':
            distance = self.y - barrier.y - barrier.height
        if direction == 'down':
            distance = barrier.y - self.y
        elif direction == 'left':
            distance = self.x - barrier.x - barrier.width
        elif direction == 'right':
            distance = barrier.x - self.x
        return distance

    # Gets direction of adjacent barrier
    def getDirection(self, barrier):
        if (barrier.x <= self.x + self.width/2 and barrier.x >= self.x - self.width/2) or (barrier.x + barrier.width <= self.x + self.width/2 and barrier.x + barrier.width >= self.x - self.width/2):
            if self.y > barrier.y:
                return 'up'
            else:
                return 'down'
        elif (barrier.y <= self.y + self.height/2 and barrier.y >= self.y - self.height/2) or (barrier.y + barrier.height <= self.y + self.height/2 and barrier.y + barrier.height >= self.y - self.height/2):
            if self.x > barrier.x:
                return 'left'
            else:
                return 'right'
        elif self.x >= barrier.x and self.x <= barrier.x + barrier.width:
            if self.y > barrier.y:
                return 'up'
            else:
                return 'down'
        elif self.y >= barrier.y and self.y <= barrier.y + barrier.height:
            if self.x > barrier.x:
                return 'left'
            else:
                return 'right'

    def turnLeft(self):
        self.angle = 90
        self._direction = 'left'

    def turnUp(self):
        self.angle = 0
        self._direction = 'up'

    def turnDown(self):
        self.angle = 180
        self._direction = 'down'

    def turnRight(self):
        self.angle = 270
        self._direction = 'right'

    def executeMove(self, move):
        if move == 'left':
            self.turnLeft()
        elif move == 'right':
            self.turnRight()
        elif move == 'up':
            self.turnUp()
        elif move == 'down':
            self.turnDown()

    #Used for Left hand on the wall with help method
    def getPreferredMoves(self, method, moves ):

        if method == 'lefthandwithhelp':
            if moves[1] == 'up':
                
            
            

    def displayWarnings(self, barrier):
        direction = self.getDirection(barrier)
        if direction != None:
            distance = self.getDistance(barrier, direction)
            if distance < 100:
                if direction == 'up':
                    self.displayWarningUp(distance)
                if direction == 'down':
                    self.displayWarningDown(distance)
                if direction == 'right':
                    self.displayWarningRight(distance)
                if direction == 'left':
                    self.displayWarningLeft(distance)

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
