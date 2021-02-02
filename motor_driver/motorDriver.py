#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

class MotorDriver:
    def __init__ (self):
        self.dirPin_R = 17      #GPIO 17, INT1
        self.dirPin_L = 27      #GPIO 27, INT2
        self.speedPin_R = 13    #GPIO 13 (PWM1), AIN1
        self.speedPin_L = 12    #GPIO 12 (PWM0), AIN2
        
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.dirPin_R, GPIO.OUT)
        GPIO.setup(self.dirPin_L, GPIO.OUT)
        GPIO.setup(self.speedPin_R, GPIO.OUT)
        GPIO.setup(self.speedPin_L, GPIO.OUT)
        
        self.piPWM_L = GPIO.PWM(self.speedPin_L, 1000)    #Creates PWM instance with frequency
        self.piPWM_R = GPIO.PWM(self.speedPin_R, 1000)    
    
    
    def motorInit(self):
        self.piPWM_L.start(0)    #starts duty cycle at 0.0 (range 0-100)
        self.piPWM_R.start(0)
       
    # Add this later
    def checkSpeed(speed):
        pass

    # Stops robot (stops PWM)
    def stop(self):
        self.piPWM_L.ChangeDutyCycle(0)
        self.piPWM_R.ChangeDutyCycle(0)
    
    # Moves both wheels forwards for 2 second then stop
    def manualForward(self, speed=30):
        self.piPWM_L.ChangeDutyCycle(speed)
        self.piPWM_R.ChangeDutyCycle(speed)
        GPIO.output(self.dirPin_L, 0)
        GPIO.output(self.dirPin_R, 1)
        sleep(2)
        self.stop()

    # Moves both wheels backwards for 2 second then stop
    def manualBackward(self, speed=30):
        self.piPWM_L.ChangeDutyCycle(speed)
        self.piPWM_R.ChangeDutyCycle(speed)
        GPIO.output(self.dirPin_L, 1)
        GPIO.output(self.dirPin_R, 0)
        sleep(2)
        self.stop()
        
    # Only moves the left wheel forward (turning right)
    #  for 2 seconds then stop
    def manualRight(self, speed=30):
        self.piPWM_L.ChangeDutyCycle(speed)
        GPIO.output(self.dirPin_L, 0)
        sleep(2)
        self.stop()
   
    # Only moves the right wheel forward (turning left)
    #  for 2 seconds then stop
    def manualLeft(self, speed=30):
        self.piPWM_R.ChangeDutyCycle(speed)
        GPIO.output(self.dirPin_R, 1)
        sleep(2)
        self.stop()

"""
    # Should probably add some speed checker here to make sure its not above 100 or below 0
    def movementInput(self, direction, speed, duration):    
        if (direction == "forward"):
            movementHandler(self, speed, speed, 0, 1, duration)
            
        elif (direction == "back"):
            movementHandler(self, speed, speed, 1, 0, duration)
        
        elif (direction == "right"):
            movementHandler(self, speed, 0, 0, 1, duration)
        
        elif (direction == "left"):
            movementHandler(self, 0, speed, 0, 1, duration)
        
        else:
            movementHandler(self, 0, 0, 0, 1, duration)
    
    # Sends commands to the motor controller (speed and direction)
    # I think we need a pull down resistor on the pins to bring the control pins down to 0V 
    # if using GPIO.cleanup()
    def movementHandler(self, speed_L, speed_R, dir_L, dir_R, duration):
        piPWM_L.ChangeDutyCycle(speed_L)
        piPWM_R.ChangeDutyCycle(speed_R)
        GPIO.output(dirPin_L, dir_L)
        GPIO.output(dirPin_R, dir_R)
        sleep(duration)
        self.stop()
"""     
