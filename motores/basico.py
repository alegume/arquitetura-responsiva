import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(5) # Initialization
try:
  while True:
    x = input('digite um valor entre 2 e 12:\n')
    p.ChangeDutyCycle(float(x))
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
