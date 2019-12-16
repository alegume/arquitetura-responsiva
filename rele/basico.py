import RPi.GPIO as GPIO
import time

PIN1 = 31
PIN2 = 33
PIN3 = 35
PIN4 = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

def ligar(x):
	print("Ligado.\n")
	GPIO.output(x, GPIO.LOW)
	time.sleep(1)

def desligar(y):
	print("Desligado.\n")
	GPIO.output(y, GPIO.HIGH)

def ligatd():
	print("Tudo ligado.\n")
	GPIO.output(PIN1, GPIO.LOW)
	GPIO.output(PIN2, GPIO.LOW)
	GPIO.output(PIN3, GPIO.LOW)
	GPIO.output(PIN4, GPIO.LOW)

def Desligatd():
	print("Tudo Desligado.\n")
	GPIO.output(PIN1, GPIO.HIGH)
	GPIO.output(PIN2, GPIO.HIGH)
	GPIO.output(PIN3, GPIO.HIGH)
	GPIO.output(PIN4, GPIO.HIGH)


ligar(PIN1)
time.sleep(1)
desligar(PIN1)


GPIO.cleanup()
