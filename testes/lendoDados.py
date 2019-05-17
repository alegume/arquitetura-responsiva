from S12 import S12

data = S12(PIN(12))

data.mesure()
temp = data.temperatura()
umi = data.umidade()

print('Temp: {}ºC'.format(temp))
print('Umi: {}%'.format(umi))