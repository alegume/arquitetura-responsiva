#!/usr/bin/python3

import smbus
import time

### Configuracoes
# Verificque o endereco com 'sudo i2cdetect -y 1'
address = 0x48
# Entradas e sensores integrados
A0 = 0x40  # Sensor de luz RDL (Resistor Dependente de Luz) (Jumper P5)
A1 = 0x41  # Sensor de temperatura integrada (Jumper P4)
A2 = 0x42  # Entrada analógica normal (sem esteroide)
A3 = 0x43  # Potenciometro  (Jumper P6)
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)
###

''' Lembretes
UMIDADE (Entrada A2 e A3) # Entrada analógica normal (sem esteroide)
	Em 5V
		Completamente seco = [249, 251]
		Completamente molhado ~= [35, 40]

	Em 3.3V
		Completamente seco = 255
		Completamente molhado ~= [12, 16] || [16, 22]

lUZ A0
	Bastante escuro (mas não escuridão total) >= ~225
	Sala com 9 luzes brancas fria = [145, 148]
	Flash muito forte = [24, 30]

Temperatura (medido com sensor DS18B20)
	18~19 C = 255??

#Volts = value * 3.3 / 255
'''

while True:
	sensors = dict(zip(['Luz', 'Temperatura'],\
		[A0, A1]))
	for descricao, entrada in sensors.items():
		bus.write_byte(address, entrada)
		bus.read_byte(address) # Dummy read (workaraound)
		value = bus.read_byte(address)
		print('{}  -> {}  \n'.format(descricao, value))

	analogic_in = dict(zip(['Umidade 1', 'Umidade 2'],\
		[A2, A3]))
	for descricao, entrada in analogic_in.items():
		bus.write_byte(address, entrada)
		bus.read_byte(address) # Dummy read (workaraound)
		value = bus.read_byte(address)
		print('{}  -> {}  \n'.format(descricao, value))


	print('-' * 35)
	time.sleep(1.5)
