import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
servo_pin=18
GPIO.setup(servo_pin, GPIO.OUT)
pwm=GPIO.PWM(servo_pin,50)
pwm.start(5)

def pixuim():
    for i in range(60, 2, -1):
        pwm.ChangeDutyCycle(i/5+2)
        time.sleep(.3)

pixuim()

pwm.stop()
GPIO.cleanup()



