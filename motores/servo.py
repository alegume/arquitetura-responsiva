#Autor: Simon Monk

import RPi.GPIO as GPIO
import time

servo_pin = 8

#Ajuste estes valores para obter o intervalo completo do movimento do servo
deg_0_pulse   = 1
deg_180_pulse = 2
f = 50.0

# Faca alguns calculos dos parametros da largura do pulso
period = 1000/f
k      = 100/period
deg_0_duty = deg_0_pulse*k
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k

#Iniciar o pino gpio
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,f)
pwm.start(11)


#time.sleep(2)

def set_angle(angle):
	duty = deg_0_duty + (float(angle)/180.0)* duty_range
	pwm.ChangeDutyCycle(duty)

try:
	for i in range(11, 2, -1):
		#angle = input("Enter angle (0 a 180): ")
		#set_angle(angle)
		pwm.ChangeDutyCycle(i)
		time.sleep(0.2)
	GPIO.cleanup()
except KeyboardInterrupt: 
	GPIO.cleanup()
