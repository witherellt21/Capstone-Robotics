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
    while True:
        
        time.sleep(0.5)
        distance1 = distance(17, 16)`
        distance2 = distance(18, 13)
        distance3 = distance(27, 12)
        distance4 = distance(22, 6)
        distance5 = distance(23, 5)
    
        print(str(distance1)+ " " +str(distance2)+ " " +str(distance3)+ " " +str(distance4)+ " " +str(distance5))
        