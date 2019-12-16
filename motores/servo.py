import RPi.GPIO as GPIO
import time

servoPIN = 18

def abrir(x=2, y=12):
	#print('ABRIR TELHADO')
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servoPIN, GPIO.OUT)
	p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
	p.start(x)
	#time.sleep(1)
	passo = 5
	fim = (y - x) * passo + 1

	for i in range(0, fim):
		p.ChangeDutyCycle(float(x+i/passo))
		#print(float(x+i/passo))
		time.sleep(0.08)

	# Encerra
	time.sleep(1)
	p.stop()
	GPIO.cleanup()

def fechar(x=12, y=2):
	#print('FECHAR TELHADO')
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(servoPIN, GPIO.OUT)
	p = GPIO.PWM(servoPIN, 50) # GPIO 18 for PWM with 50Hz
	p.start(x)
	#time.sleep(1)
	passo = 5
	fim = (x - y) * passo + 1
	#print('fim:', fim)

	for i in range(0, fim):
		p.ChangeDutyCycle(float(x-i/passo))
		#print(float(x-i/passo))
		time.sleep(0.08)

	# Encerra
	time.sleep(1)
	p.stop()
	GPIO.cleanup()
