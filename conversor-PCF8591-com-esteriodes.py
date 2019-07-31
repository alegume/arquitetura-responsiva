#!/usr/bin/python3

import smbus
import os
import time
import socket
from datetime import datetime
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

### Configuracoes
# Verifique o endereco com 'sudo i2cdetect -y 1'
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
	Em 3.3V
		Completamente seco ~= [20, 27]
		Completamente molhado ~= [250, 255]

LUZ A0
	Bastante escuro (mas não escuridão total) ~=
	Luz em ambiente interno durante o dia ~= 130
	Sala com 9 luzes brancas fria ~= 150
	Flash muito forte >= 220

Temperatura (medido com sensor DS18B20)
	18~19 C = 255??

#Volts = value * 3.3 / 255
'''

'''
Vaso C
	(semana passada) -> 25, 31


Vaso A
	(semana passada) -> 40, 48
	50ml -> 214, 248
	50ml -> 267, 278

Vaso B
	25ml -> 108, 185


'''

LUZ_ABRIR = 100
UMIDADE_IRRIGAR = 150

# Informacoes do host
dir_path = os.path.dirname(os.path.realpath(__file__))
hostname = socket.gethostname()

# Credenciais do Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(dir_path, 'secret_key.json'), scope)
client = gspread.authorize(creds)
# Abre um documeto (spreadsheet)
spreadsheet = client.open(hostname)

def log_local(row):
	try:
		with open(os.path.join(dir_path, 'log.csv'), 'a') as f:
			w = csv.writer(f)
			w.writerow(row)
	except Exception as e:
		print(e)
		print('Erro ao salvar dado em arquivo .csv')

def log_nuvem(row):
	# Todas as worksheets
	try:
		worksheet = spreadsheet.worksheet('dados-sensores')

	except Exception as e:
		print(e)
		print('Erro ao abrir worksheet')

	try:
		worksheet.append_row(row)
	except Exception as e:
		print(e)
		print('Erro ao enviar dados para a nuvem')

def main():
	sensores = dict(
		zip(
			['Luz', 'Temperatura', 'Umidade1', 'Umidade2'],
			[A0, A1, A2, A3]
		)
	)

	hora = datetime.now().strftime('%d/%m/%Y %H:%M:%-S')
	dados = {}
	for descricao, entrada in sensores.items():
		try:
			bus.write_byte(address, entrada)
			# Primeira amostra eh descartada (workaraound)
			bus.read_byte(address)
			# Leitura e ajuste empírico
			value = (bus.read_byte(address) - 280) * -1

			# data e hora, luz, temperatura, umidade1, umidade2
			dados[descricao] = value
			print('{}  -> {}  \n'.format(descricao, value))
		except Exception as e:
			print(e)
			print('Erro ao ler entrada ', entrada)

	# Ações a serem executadas
	#abrir_telhado = irrigar = False
	if dados['Luz'] > LUZ_ABRIR:
		abrir_telhado = 'Abrir telhado'
	else:
		abrir_telhado = 'Fechar telhado'

	if dados['Umidade2'] < UMIDADE_IRRIGAR: # or dados['Umidade1'] < UMIDADE_IRRIGAR:
		irrigar = 'Sim'
	else:
		irrigar = 'Não'

	print('Telhado  -> {}  \n'.format(abrir_telhado))
	print('Irrigar  -> {}  \n'.format(irrigar))

	# Dados para gerar logs
	row = [hora, dados['Luz'], dados['Temperatura'], dados['Umidade1'], dados['Umidade2'], abrir_telhado, irrigar]

	log_local(row)
	log_nuvem(row)

if __name__ == '__main__':
	main()
