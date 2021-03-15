from gpiozero import Servo
import time

def FaceForward():
   s = Servo(18, min_pulse_width = 0.5/1000, max_pulse_width = 10/1000, frame_width = 20/1000)
   s.max()
   time.sleep(1)
   s.detach()
   time.sleep(1)

def FaceBackward():
   s = Servo(18, min_pulse_width = 0.5/1000, max_pulse_width = 10/1000, frame_width = 20/1000)
   s.min()
   time.sleep(1)
   s.detach()
   time.sleep(1)


def FaceRight():
   s = Servo(18, min_pulse_width = 1.1/1000, max_pulse_width = 10/1000, frame_width = 20/1000)
   s.min()
   time.sleep(1)
   s.detach()
   time.sleep(1)

def FaceLeft():
   s = Servo(18, min_pulse_width = 1/1000, max_pulse_width = 10/1000, frame_width = 20/1000)
   s.max()
   time.sleep(1)
   s.detach()
   time.sleep(1)

