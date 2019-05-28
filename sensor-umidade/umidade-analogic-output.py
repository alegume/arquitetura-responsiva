#!/usr/bin/python3

import smbus
import time

#check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

while True:
	bus.write_byte(address, A0)
	value = bus.read_byte(address)
	print('AOUT:{}  '.format(value * 3.3 / 255))
	time.sleep(0.1)
