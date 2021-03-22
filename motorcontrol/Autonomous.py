import RPi.GPIO as GPIO
import time

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
    
    distance = (TimeElapsed * 34300) / 2
    
    return distance



    
if __name__=='__main__':
    GPIO.cleanup()
    while True:
        #front= distance(16, 17)
        time.sleep(.1)
        #left = distance(13, 18)
        time.sleep(.1)
        #right = distance(12,27)
        time.sleep(.1)
#         distance4 = distance(22, 6)
#         distance5 = distance(23, 5)
    
        print(str(left) + ' ' + str(front) + ' ' + str(right))
        