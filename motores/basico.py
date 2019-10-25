import RPi.GPIO as GPIO
import time

servoPIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(5) # Initialization
try:
  while True:
    x = input('duty cycle:\n')
    p.ChangeDutyCycle(float(x))
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
