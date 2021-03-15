import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

class Arm():

    def __init__(self, _address):
        self.kit = MotorKit(address = _address)
        self.kit.stepper1.release()
        
        self.status = 'up'

    def armUp(self):
        for i in range(80):
            self.kit.stepper1.onestep(direction = stepper.BACKWARD, style = stepper.SINGLE)
            time.sleep(0.005)
        
    def armDown(self):
        for i in range(90):
            self.kit.stepper1.onestep(direction = stepper.FORWARD, style = stepper.SINGLE)
            time.sleep(0.005)
            
    def openClaw(self):
        self.kit.motor3.throttle = 1.0
        time.sleep(0.3)
        self.kit.motor3.throttle = 0
        
    def closeClaw(self):
        self.kit.motor3.throttle = -0.75
        time.sleep(0.3)
        self.kit.motor3.throttle = 0


def main():
    choice = 'Y'
    while choice == 'Y':
        direction = input("Do you want to move the arm up (u) or down (d): ")
        
        if direction == 'u':
            doubleStepUp()
        elif direction == 'd':
            doubleStepDown()
            kit.stepper1.release()
        else:
            choice = input("Hit Y to give new instruction or anything else to quit")


if __name__ == "__main__":
    main()
