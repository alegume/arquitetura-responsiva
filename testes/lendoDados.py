#from S12 import S12

#data = S12(PIN(12))

#data.mesure()
#temp = data.temperatura()
#eva = data.evaporacao()
#veloVento = data.velocidadeDoVento()
#rad = data.radiacao()

#print('Temp: {}ºC'.format(temp))
#print('Umi: {}%'.format(umi))

file_name = "todas_estacoes_automaticas"

f = open("../ProjetoProjetoArquiteturaResponsiva-master/testes/"+file_name)
text = f.readlines()
station_numbers = []

for t in text:
	if ""