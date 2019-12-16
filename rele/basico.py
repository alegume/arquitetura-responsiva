import RPi.GPIO as GPIO
import time

PIN1 = 6
PIN2 = 13
PIN3 = 19
PIN4 = 26


GPIO.setwarnings(False)


def ligar(x):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(x, GPIO.OUT)
	GPIO.output(x, GPIO.LOW)
	time.sleep(1)

def desligar(y):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(y, GPIO.OUT)
	GPIO.output(y, GPIO.HIGH)
	GPIO.cleanup()

def ligatd():
	GPIO.output(PIN1, GPIO.LOW)
	GPIO.output(PIN2, GPIO.LOW)
	GPIO.output(PIN3, GPIO.LOW)
	GPIO.output(PIN4, GPIO.LOW)

def Desligatd():
	GPIO.output(PIN1, GPIO.HIGH)
	GPIO.output(PIN2, GPIO.HIGH)
	GPIO.output(PIN3, GPIO.HIGH)
	GPIO.output(PIN4, GPIO.HIGH)
	GPIO.cleanup()
