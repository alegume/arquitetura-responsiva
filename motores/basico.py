import RPi.GPIO as GPIO
import time

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
x = input('start:\n')
p.start(float(5)) # Initialization
try:
  while True:
    x = input('duty cycle:\n')
    p.ChangeDutyCycle(float(x))
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
