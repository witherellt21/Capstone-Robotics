"""
Author: Nick St. Pierre
Filename: main.py
Description: Test for the motors
"""

from adafruit_motorkit import MotorKit
import pygame, time, board
from throttleFunctions import *
from adafruit_motor import stepper

motorKit = MotorKit(address = 0x60)
arm = MotorKit(i2c = board.I2C(), address = 0x61)

arm.stepper1.release()

def armUp():
    for i in range(80):
        arm.stepper1.onestep(direction = stepper.BACKWARD, style = stepper.DOUBLE)
        time.sleep(0.005)
        
def armDown():
    for i in range(90):
        arm.stepper1.onestep(direction = stepper.FORWARD, style = stepper.SINGLE)
        time.sleep(0.005)
        
def openClaw():
    arm.motor3.throttle = 1.0
    time.sleep(0.3)
    arm.motor3.throttle = 0
    
def closeClaw():
    arm.motor3.throttle = -0.75
    time.sleep(0.3)
    arm.motor3.throttle = 0

def rightTurn(motorKit, throttle):
    "Performs a right turn"
    motorKit.motor1.throttle = throttle
    motorKit.motor2.throttle = -throttle
    motorKit.motor3.throttle = throttle
    motorKit.motor4.throttle = -throttle

def leftTurn(motorKit, throttle):
    "Performs a right turn"
    motorKit.motor1.throttle = throttle
    motorKit.motor2.throttle = -throttle
    motorKit.motor3.throttle = throttle
    motorKit.motor4.throttle = -throttle

def throttleUp(motorKit, motor, voltage):
    "Increases the initial voltage for the motors"
    motorKit.motor.throttle = 1.0
    time.sleep(0.2)
    motorKit.motor.throttle = voltage

def stop(motorKit):
    "Sets the voltages of the motors to 0."
    motorKit.motor1.throttle = 0
    motorKit.motor2.throttle = 0
    motorKit.motor3.throttle = 0
    motorKit.motor4.throttle = 0

def forward(motorKit):
    "Places the motors in a forward motion."
    motorKit.motor1.throttle = 0.8
    motorKit.motor2.throttle = -0.8
    motorKit.motor3.throttle = 0.8
    motorKit.motor4.throttle = -0.8


SCREEN_SIZE = (100,100)

def main():
    RUNNING = True
    pygame.init()
    pygame.display.set_caption("Motor Test")
    screen = pygame.display.set_mode(list(SCREEN_SIZE))

    robot = MotorKit(address = 0x60)
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #accelerateLinear(robot, "forward")
                    #accelerateExp(robot, "forward")
                    #accelerateLog(robot, "forward")
                    robot.motor1.throttle = 1.0
                    robot.motor2.throttle = 1.0
                    #robot.motor3.throttle = 0.8
                    #robot.motor4.throttle = 0.8
                elif event.key == pygame.K_DOWN:
                    #accelerateLinear(robot, "backward")
                    #accelerateExp(robot, "backward")
                    #accelerateLog(robot, "backward")
                    robot.motor1.throttle = -1.0
                    robot.motor2.throttle = -1.0
                    #robot.motor3.throttle = -0.8
                    #robot.motor4.throttle = -0.8
                elif event.key == pygame.K_RIGHT:
                    robot.motor1.throttle = 1.0
                    robot.motor2.throttle = -1.0
                    #robot.motor3.throttle = 0.8
                    #robot.motor4.throttle = 0.0
                elif event.key == pygame.K_LEFT:
                    robot.motor1.throttle = -1.0
                    robot.motor2.throttle = 1.0
                    #robot.motor3.throttle = 0.0
                    #robot.motor4.throttle = 0.8
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    #decelerateLinear(robot, "forward")
                    #decelerateExp(robot, "forward")
                    #decelerateLog(robot, "forward")
                    stop(robot)
                elif event.key == pygame.K_DOWN:
                    #decelerateLinear(robot, "backward")
                    #decelerateExp(robot, "backward")
                    #decelerateLog(robot, "backward")
                    stop(robot)
                elif event.key == pygame.K_LEFT:
                    stop(robot)
                elif event.key == pygame.K_RIGHT:
                    stop(robot)
                else:      
                    more = input('hit y for arm controls: ')
                    while more == 'y':
                        arm.stepper1.release()
                        direction = input('u, d, o, c: ')
                        if direction == 'u':
                            armUp()
                        elif direction == 'd':
                            armDown()
                        elif direction == 'o':
                            openClaw()
                        elif direction == 'c':
                            closeClaw()
                        arm.stepper1.release()
                        more = input('y for more: ')
                    arm.stepper1.release()


    pygame.quit()

if __name__ == "__main__":
    main()
