#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

#motorPWMpin = 12
#assigning pins for motor speed pins and GPIO digital "in" pins
dirPin_R = 17       #GPIO 17, INT1
dirPin_L = 27       #GPIO 27, INT2
speedPin_R = 13     #GPIO 13 (PWM1), AIN1
speedPin_L = 12     #GPIO 12 (PWM0), AIN2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#GPIO.setup(motorPWMpin, GPIO.OUT)
GPIO.setup(dirPin_R, GPIO.OUT)
GPIO.setup(dirPin_L, GPIO.OUT)
GPIO.setup(speedPin_R, GPIO.OUT)
GPIO.setup(speedPin_L, GPIO.OUT)


piPWM_L = GPIO.PWM(speedPin_L, 1000)    #create PWM instance with frequency
piPWM_L.start(0)     #starts duty cycle at 0.0 (range 0-100)
                    #pwm cycle for rasp pi is 100
piPWM_R = GPIO.PWM(speedPin_R, 1000)
piPWM_R.start(0)

try:
    while(1):
            leftSpeed = input("Left speed? ")
            rightSpeed = input("Right speed? ")
            print "leftSpeed: ", leftSpeed
            print "rightSpeed: ", rightSpeed
           
            # Moving left forwards
            if (leftSpeed >= 0):
                if(leftSpeed > 100):            #max speed = 100
                    leftSpeed = 100
                piPWM_L.ChangeDutyCycle(leftSpeed)
                GPIO.output(dirPin_L, 0)
            
            # Moving left backwards
            elif (leftSpeed < 0):
                if(leftSpeed < -100):
                    leftSpeed = -100
                piPWM_L.ChangeDutyCycle(leftSpeed * -1)
                GPIO.output(dirPin_L, 1);

            # Moving right forwards
            if (rightSpeed >= 0):
                if(rightSpeed > 100):            #max speed = 100
                    leftSpeed = 100
                piPWM_R.ChangeDutyCycle(rightSpeed)
                GPIO.output(dirPin_R, 1)
            
            # Moving right backwards
            elif (rightSpeed < 0):
                if(rightSpeed < -100):
                    rightSpeed = -100
                piPWM_R.ChangeDutyCycle(rightSpeed * -1)
                GPIO.output(dirPin_R, 0);
            
            for i in range(3):
                print "Waiting... " + str(i+1)
                sleep(1)

            piPWM_R.ChangeDutyCycle(0);
            piPWM_L.ChangeDutyCycle(0);

    
    """
    while(1):
        for duty in range(0,101,1):
            pi_PWM.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)

        for duty in range (100, -1, -1):
            pi_PWM.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)
    """

#need to figure out how to shutdown properly
# when hiting ctrl+C, the wheels start turning,
# not sure why
except KeyboardInterrupt:
    piPWM_L.stop()
    GPIO.cleanup()





#Change frequency:
#pi_PWM.ChangeFruency(freq) where frez is the new frequency in hz

#change duty cycle:
#pi_PWM.ChangeDutyCycle(dc) where 0.0 <= dc <= 100.0

#stop PWM:
#pi_PWM.stop()


        

