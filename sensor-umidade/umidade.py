#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

# Numeracao dos PINS -> BCM
GPIO.setmode(GPIO.BCM)
# Porta conectada
PORTA = 17
# Entrada
GPIO.setup(PORTA, GPIO.IN)

def callback(PORTA):
	if GPIO.input(PORTA):
		print("\tSuave!")
	else:
		print("\tPor favor, me molhe *-*")

# Adiciona de evento HIGH ou LOW
GPIO.add_event_detect(PORTA, GPIO.BOTH, bouncetime=300)
# Adiciona o callback do evento
GPIO.add_event_callback(PORTA, callback)

# Deixa o script rodando sempre
while True:
	time.sleep(0.5)
