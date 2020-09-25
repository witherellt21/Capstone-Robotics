from motor import Motor
from automobile import Automobile


fl = Motor(4)
fr = Motor(17)
br = Motor(22)
bl = Motor(27)

robot = Automobile(fr, br, fl, bl)

while True:
    fl.forward()
    #robot.drive()