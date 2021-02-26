import time
import boardfrom adafruit_motorkit
import MotorKitfrom adafruit_motor
import stepper

kit = MotorKit(i2c=board.I2C())
kit.stepper1.release()

def doubleStepUp():
    for i in range(80):
        kit.stepper1.onestep(direction=FORWARD, style=DOUBLE)
        time.sleep(.002)

def doubleStepDown():
    for i in range(60):
        kit.stepper1.onestep(direction=BACKWARD, style=DOUBLE)
        time.sleep(.002)

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
