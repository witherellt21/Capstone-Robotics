import RPi.GPIO as GPIO
import time
import board
from adafruit_motorkit import MotorKit
from turnFunctions import robotManuevers as rm
#from usfs import USFS_Master

GPIO.setmode(GPIO.BCM)

wheels = MotorKit(i2c = board.I2C())

def distance(trig, echo):
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)
    
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(echo) == 0:
        StartTime = time.time()
    
    while GPIO.input(echo) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    
    distance = (TimeElapsed * 34300) / 2
    
    return distance

def leftHand():
    if left > 50:
        print("turning left")
        rm.turnLeft90()
    elif front > 50:
        print("going straight")
        rm.goStraight()
    elif right > 50:
        print("turning right")
        rm.turnRight90()
    else:
        print("turning around")
        rm.turnAround()

def turnTracking ():
    
    leftCount = 0
    rightCount = 0
    
    if leftCount == 0 and left > 50:
        print("turning left")
        rm.turnLeft90()
        leftCount += 1
    if leftCount == 1 and rightCount == 0 and right > 50:
        print("turning right")
        rm.turnRight90()
        rightCount += 1
    if leftCount == 1 and rightCount == 1 and right > 50:
        print("turning right")
        rm.turnRight90()
        rightCount += 1
    if leftCount == 1 and rightCount == 2 and left > 50:
        print("turning left")
        rm.turnLeft90()
        leftCount += 1
    if leftCount == 2 and rightCount == 2 and left > 50:
        print("turning left")
        rm.turnLeft90()
        leftCount += 1
    if leftCount == 3 and rightCount == 2 and right > 50:
        print("turning right")
        rm.turnRight90()
        rightCount += 1  
    if leftCount == 3 and rightCount == 3 and right > 50:
        print("turning right")
        rm.turnRight90()
        rightCount += 1
    if leftCount == 3 and rightCount == 4 and left > 50:
        print("turning left")
        rm.turnLeft90()
        leftCount += 1
# if usfs_active:
#     MAG_RATE = 100
#     ACCEL_RATE = 200
#     GYRO_RATE = 200
#     BARO_RATE = 50
#     Q_RATE_DIVISOR = 3
# 
#     usfs = USFS_Master(MAG_RATE, ACCEL_RATE, GYRO_RATE, BARO_RATE, Q_RATE_DIVISOR)
# 
#     if not usfs.begin():
#         print(usfs.getErrorString())
#         exit(1)
# 
#     usfs.checkEventStatus()
# 
#     if usfs.gotError():
#         print('ERROR: ' + usfs.getErrorString())
#         exit(1)
# 
# def getYaw():
# 
#     if (usfs.gotQuaternion()):
# 
#             qw, qx, qy, qz = usfs.readQuaternion()
# 
#             yaw = math.atan2(2.0 * (qx * qy + qw * qz), qw * qw + qx * qx - qy * qy - qz * qz)
# 
#             yaw *= 180.0 / math.pi
#             yaw += 9.1
#             if yaw < 0: yaw += 360.0
# 
#             return yaw

if __name__=='__main__':
    GPIO.cleanup()
    while True:
        front= distance(16, 17)
        time.sleep(.1)
        left = distance(13, 18)
        time.sleep(.1)
        right = distance(12,27)
        time.sleep(.1)
#         distance4 = distance(22, 6)
#         distance5 = distance(23, 5)
        leftHand()
    
        print(str(left) + ' ' + str(front) + ' ' + str(right))
        