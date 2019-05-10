import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
PORTA = 14
GPIO.setup(PORTA, GPIO.OUT) # Define o PIN 18 como saida

def ligar():
	print('Ligado')
	GPIO.output(PORTA, GPIO.HIGH)


def desligar():
	print('Desligado')
	GPIO.output(PORTA, GPIO.LOW)

comando = 0
while (comando != -1):
	print("Digite um valor (0=Desligado; 1=Ligado; -1=Terminar)")
	comando = int(input())
	if (comando == 1):
		ligar()
	elif (comando == 0):
		desligar()

# Forcar desligar no final
desligar()





