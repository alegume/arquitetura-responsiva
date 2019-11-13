import RPi.GPIO as GPIO
import time

servoPIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

start = 12
end = 2
start = float(input('Digite o inicio (2, 12):\n'))

p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
p.start(start) # Initialization
try:
  while True:
    end = input('Digite a posição (2, 12):\n')
    p.ChangeDutyCycle(float(end))
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
