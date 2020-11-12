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
        self.direction = 'up'
        self.center = (self.x, self.y)
        self.surface = pygame.Surface((self.width, self.height))

    def draw(self, degrees):

        angle = math.pi*degrees/180

        #if self.direction == 'up':
        point_of_triangle = (self.x + self.height/2 * math.cos(math.pi*90/180 + angle), (self.y - self.height/2 * math.sin(math.pi*90/180 + angle)))
        bottom_left = (self.x + self.height/2 * math.cos(math.pi*225/180 + angle), self.y - self.height/2 * math.sin(math.pi*225/180 + angle))
        bottom_right = (self.x + self.height/2 * math.cos(math.pi*315/180 + angle), self.y - self.height/2 * math.sin(math.pi*315/180 + angle))
        coordinates = [bottom_left, point_of_triangle, bottom_right]
        '''
        elif self.direction == 'left':
            point_of_triangle = (self.x - self.width/2, self.y)
            coordinates = [(self.x + self.height/2, self.y - self.width/2), point_of_triangle, (self.x + self.height/2, self.y + self.width/2)]
        elif self.direction == 'right':
            point_of_triangle = (self.x + self.width/2, self.y)
            coordinates = [(self.x - self.height/2, self.y - self.width/2), point_of_triangle, (self.x - self.height/2, self.y + self.width/2)]
        elif self.direction == 'down':
            point_of_triangle = (self.x, (self.y + self.height/2))
            coordinates = [(self.x - self.width/2, self.y - self.height/2), point_of_triangle, (self.x + self.width/2, self.y - self.height/2)]
        '''
        #pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height),0)
        pygame.draw.polygon(self.screen, self.color, coordinates)

    def getDistance(self, barrier, direction):
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
