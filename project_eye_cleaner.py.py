import RPi.GPIO as GPIO           # import RPi.GPIO module  
import time
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
GPIO.setup(2, GPIO.OUT) 
GPIO.setup(3, GPIO.OUT) 


GPIO.output(2, 1)        
GPIO.output(3, 0)       
time.sleep(5)
GPIO.output(2, 0)        
GPIO.output(3, 1) 
time.sleep(5)
GPIO.output(2, 0)        
GPIO.output(3, 0) 