import time
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

class Arm:

    def __init__(self):
        kit = MotorKit(i2c=board.I2C())
        kit.stepper1.release()

    def doubleStepUp(self):
        for i in range(100):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
            time.sleep(.0025)

    def doubleStepDown(self):
        for i in range(80):
            kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
            time.sleep(.005)


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
