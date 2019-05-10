#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

# Numeracao dos PINS -> BCM
GPIO.setmode(GPIO.BCM)
# Porta como entrada entrada
PORTA = 14
GPIO.setup(PORTA, GPIO.IN)

def callback(PORTA):
	#print('\nValor: ', GPIO.input(PORTA))
	if GPIO.input(PORTA):
		print('\tPor favor, me molhe *-*')
	else:
		print('\tSuave!!')

# Chama na alta
callback(PORTA)
# Adiciona de evento HIGH ou LOW
GPIO.add_event_detect(PORTA, GPIO.BOTH, bouncetime=300)
# Adiciona o callback do evento
GPIO.add_event_callback(PORTA, callback)

# Deixa o script rodando sempre
while True:
	time.sleep(1)
