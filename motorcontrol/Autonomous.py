import RPi.GPIO as GPIO
import time
import board
from adafruit_motorkit import MotorKit
from turnFunctions import robotManuevers as rm
#from usfs import USFS_Master

GPIO.setmode(GPIO.BCM)



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
    
    distance = (TimeElapsed * 34300*0.393701) / 2
    
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
    
    
    time.sleep(0.5)
    left = distance(5, 17)
    front = distance(6, 18)
    right = distance(12, 27)
    backRight = distance(13, 22)
    backLeft = distance(16, 23)

    print(str(left)+ " " +str(front)+ " " +str(right)+" " +str(backRight) + " " +str(backLeft))
    
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

def turnTrackingTrial():
    
    rm.stopMoving()
    
    leftCount = 0
    rightCount = 0
    turnCount = 0
    fCount = 0
    while True:
        time.sleep(0.5)
        left = distance(5, 17)
        front = distance(6, 18)
        right = distance(12, 27)
#         backRight = distance(13, 22)
#         backLeft = distance(16, 23)
        print(str(left)+ " " +str(front)+ " " +str(right))



        if turnCount == 0:
            if front > 9:
                print("forward")
                rm.goStraight()
            if front<9 and left<40 and right>20:
                rm.turnRight90()
                print("right")
                turnCount+=1
        elif turnCount == 1:
            if front > 13:
                print("forward")
                rm.goStraight()
            if front <13 and left>20:
                rm.turnLeft90()
                print("left")
                turnCount+=1
                
        elif turnCount == 2:
            if front>9:
                print("forward")
                rm.goStraight()
            if front<9 and right>10:
                rm.turnRight90()
                print("right")
                turnCount+=1
        elif turnCount ==3:
            if front>11.2:
                print("forward")
                rm.goStraight()
            if front<11.2 and left>25:
                rm.turnLeft90Over()
                print("left")
                turnCount += 1
        elif turnCount==4:
            if front>5:
                rm.goStraight()
                print("forward")
            else:
                rm.stopMoving()
                break
    

                
        

    


if __name__=='__main__':
    GPIO.cleanup()
    #turnTrackingTrial()
#     while True:
#         time.sleep(0.5)
#         left = distance(5, 17)
#         front = distance(6, 18)
#         right = distance(12, 27)
# 
#         print(str(left)+ " " +str(front)+ " " +str(right))
#     while True:
#         turn = input("l, r, or o")
#         if turn == 's':
#             rm.goStraight()
#         elif turn =='r':
#             rm.turnRight90()
#         elif turn == 'o':
#             rm.turnLeft90Over()
#         else:
#             break
   
            
        
#         front= distance(16, 17)
#         time.sleep(.1)
#         left = distance(13, 18)
#         time.sleep(.1)
#         right = distance(12,27)
#         time.sleep(.1)
# #         distance4 = distance(22, 6)
# #         distance5 = distance(23, 5)
#         leftHand()
#     
#         print(str(left) + ' ' + str(front) + ' ' + str(right))
#         