"""
Author: Nick St. Pierre and Mitchell Roberts
Filename: autonomy.py
Description: a class that inherits from robot and contains methods necessary
for autonomous decision making.
"""

class Autonomy(object):
    
    def __init__(self):
        
        # Distance Sensors Instanced
        # Data Structure: Stack through Python List
        self._rightSensor = []
        self._leftSensor = []
        self._frontSensor = []
        self._backSensor = []
        
        # LiDAR Sensor Instanced
        # Data Structure: Unknown
        
        # Proximity Sensor Instanced
        # Data Structure: Unknown
        
        # IMU Sensor Instanced
        # Data Structure: Unknown
        
    
    def distanceSensor(self, robot):
        "a method that gathers data in a manner like a distance sensor"
        pass
    
    def lidarSensor(self, robot):
        "a method that gathers data in a manner like a lidar sensor would"
        pass
    
    def proxSensor(self, robot):
        "a method that gathers data like a proximity sensor"
        pass
    
    def imuSensor(self, robot):
        "function that maintains the acceleration and rotational data"
        pass
    
    def think(self, robot):
        "function that maintains logic behind robot movement"
        # gets robot position
        # breaks down into
        
        #This file serves to structure the responses that the robot should have to receiving different input from sensors and the user
#Author: Mitchell Roberts

#The robot will likely use the following sensors
    #rangefinder or lidar
    #camera
    #accelerometer - why?

#While in RC mode:

    #Send camera live feed to the operator over the wifi

    #While the operator has opted to receive sensor data:
        # read in data from the rangefinder
            # convert the data into a usable format
        # read in accelerometer data
            # convert the data into a usable format

    #If the robot senses that it is within 12 inches of a wall in front, it should:
        #A. notify the operator of a hazard
            # use a wireless port to send message across wifi
        #B. slow down to a stop
            # send a signal to the motors controlling the wheels to lower the speed
        #C. pause in place to give the operator time to respond
            #operator should pan the camera to look around before safely executing a turn
        #D. if during the turn, the robot comes within 4 inches of the wall on any side, it should:
            # stop immeditely
            # notify the operator that they are too close to the wall

    #If the robot senses that it is within 4 inches of any side wall, it should:
        #A. cut some power to wheels driving the side of the robot furthest from the wall
        #B. send some more power to the wheels driving the side of the robot nearest the wall
        #C. notify the operator that the system is using lane assist
        #D. balance the power back out when the robot is far enough away from the wall again

#While in Autonomous mode:

    #Send camera live feed to the operator over the wifi, if allowed

    # Use "left hand on the wall" algoritm: https://www.instructables.com/id/Maze-Solving-Robot/

    #If the robot can turn left, it should
    #Else if the robot can go straight, it should
    #Else if a right turn is the only option, the robot should turn right
    #Else turn around (dead end)

    #If the forward distance < 12 inches from a wall (the robot must turn left or right):
        # slow the robot speed down
        # once the robot is within 6 inches of the wall, stop completely
        # identify the next turn using the "left hand on the wall" algorithm
            # if there is a left turn available (left distance > 16 inches):
                # turn left and continue forward
            # else if there is a right turn available (right distance > 16 inches)
                # turn right and continue forward
            # else
                # turn 180 degrees and head back the way the robot came

    #If the left side distance > 16 inches from the wall (there is a left turn available):
        # stop the robot after brief delay to clear the corner of the wall
        # execute the left turn and continue straight