#!/usr/bin/python

import PCF8591 as ADC

ADC.setup(0x48)

def loop():
	while True:
		print(ADC.read(2))
		ADC.write(ADC.read(0))

def destroy():
	ADC.write(0)

if __name__ == "__main__":
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
