#!/usr/bin/python3

import smbus
import time

### Configs
#check your PCF8591 address by type in 'sudo i2cdetect -y 1' in terminal.
address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)
###

''' Lembretes
PARECE QUE SÓ A2 ESTÁ FUNCIONANDO!!!!!!!!!!!!!!!!!
Em 5V
	Completamente seco = [249, 251]
	Completamente molhado ~= [35, 40]

Em 3.3V
	Completamente seco = 255
	Completamente molhado ~= [12, 16] || [16, 22]

#Volts = value * 3.3 / 255
'''

while True:
	for A in [A0, A1, A2, A3]:
		bus.write_byte(address, A)
		bus.read_byte(address) # Dummy read (workaraound)
		value = bus.read_byte(address)
		print('{}  -> {}  '.format(A, value))
	print('\n')
	time.sleep(1)
