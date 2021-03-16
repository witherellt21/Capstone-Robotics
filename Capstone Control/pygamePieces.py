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

    def draw(self, _angle):

        angle = math.pi*_angle/180

        angle = math.pi*_angle/180
        
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
                pass
                
            
            

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

class LaneRobot():

    def __init__(self, screen, x, y, height, width, color, pixels_per_inch):
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

        self.ppi = pixels_per_inch

    def draw(self):
        
        coordinates = (self.x-self.width/2, self.y-self.height/2, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, pygame.Rect(coordinates))
        

    def drawBarriers(self,front, left, right, back):

        barrier_thickness = 1.5*self.ppi
        
        #Draw front barrier
        front_coords = (self.x-self.width/2, self.y-self.height/2 - barrier_thickness - front*self.ppi, self.width, barrier_thickness)
        pygame.draw.rect(self.screen, (150, 150, 255), pygame.Rect(front_coords))

        #Draw left barrier
        left_coords = (self.x-self.width/2 - barrier_thickness - left*self.ppi, self.y-self.height/2, barrier_thickness, self.height)
        pygame.draw.rect(self.screen, (150, 150, 255), pygame.Rect(left_coords))

        #Draw right barrier
        right_coords = (self.x+self.width/2 + right*self.ppi, self.y-self.height/2, barrier_thickness, self.height)
        pygame.draw.rect(self.screen, (150, 150, 255), pygame.Rect(right_coords))

        #Draw back barrier
        back_coords = (self.x-self.width/2, self.y+self.height/2 + back*self.ppi, self.width, barrier_thickness)
        pygame.draw.rect(self.screen, (150, 150, 255), pygame.Rect(back_coords))

class Cockpit():

    def __init__(self, screen, x, y, height, width):

        self.screen = screen
        self.height = height
        self.width = width

        #self.center = self.x + self. heig

    def drawThrottles(self, m1, m2):

        offset= -10
        angle = math.tanh((self.width/15)/(self.height*40/50))

        self.height*45/50 - m1 * self.height*40/50

        width_m1 = (self.height*45/50-(self.height* 45/50 - m1 * self.height*40/50)) *math.tan(angle)
        width_m2 = (self.height*45/50-(self.height* 45/50 - m2 * self.height*40/50)) *math.tan(angle)


        point_of_triangle = (self.width /6, self.height * 45/50 - offset)
        top_left = (self.width/6 - width_m1, self.height* 45/50 - m1 * self.height*40/50 -offset )
        top_right = (self.width/6 + width_m1, self.height* 45/50 - m1 * self.height*40/50 -offset)
        coordinates = [top_left, point_of_triangle, top_right]

        m2_point_of_triangle = (self.width *4/10, self.height * 45/50 - offset)
        
        m2_top_left = (self.width*4/10-width_m2, self.height* 45/50 - m2 * self.height*40/50 - offset)
        m2_top_right = (self.width*4/10+width_m2, self.height* 45/50 - m2 * self.height*40/50 - offset)
        m2_coordinates = [m2_top_left, m2_point_of_triangle, m2_top_right]

        pygame.draw.polygon(self.screen, (255, (1-m1)*255, 0), coordinates)
        pygame.draw.polygon(self.screen, (255, (1-m2)*255, 0), m2_coordinates)

    def drawIntensity(self, intensity):
        pass
        


class Compass():

    def __init__(self, screen, x, y, height, width):
        self.screen = screen
        self.height = height
        self.width = width

    def drawCompass(self, orientation):

        steps = 20
        tick_spacing = 2*math.pi/steps

        angle = 0
        while angle <= 2*math.pi:

            x = math.cos(angle)
            y = math.sin(angle)

            radius = self.width/3
            radius2 = self.width/3 + 8
            
            bottom_right = (self.width/2 + math.cos(angle-.01)*radius, self.height/2 - math.sin(angle-0.01)*radius)
            bottom_left = (self.width/2 + math.cos(angle+.01)*radius, self.height/2 - math.sin(angle+0.01)*radius)
            top_right = (self.width/2 + math.cos(angle-.01)*radius2, self.height/2 - math.sin(angle-0.01)*radius2)
            top_left = (self.width/2 + math.cos(angle+.01)*radius2, self.height/2 - math.sin(angle+0.01)*radius2)

            coordinates = (top_left, bottom_left, bottom_right, top_right)
            pygame.draw.polygon(self.screen, (255, 255, 255), coordinates)

            angle += tick_spacing


        bottom_right = (self.width/2 + math.cos(orientation-math.pi/2)*8, self.height/2 - math.sin(orientation-math.pi/2)*8)
        bottom_left = (self.width/2 + math.cos(orientation+math.pi/2)*8, self.height/2 - math.sin(orientation+math.pi/2)*8)
        top = (self.width/2 + math.cos(orientation)*100, self.height/2 - math.sin(orientation)*100)

        coordinates = (bottom_right, top, bottom_left)

        pygame.draw.polygon(self.screen, (255, 0 , 0), coordinates)

            

            

            

        
        

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
