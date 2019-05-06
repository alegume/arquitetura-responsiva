import requests
from bs4 import BeautifulSoup

vq_home_request = requests.get('http://www.ciram.sc.gov.br/agroconnect/')
vq_home_content = vq_home_requests.text
#vq_home_content

#html da pagina aqui

operation_column = soup.find(class_="page-quick-sidebar station-data")
#extraindo informação da classe onde enontra-se os dados da estação


nearby_city = ['Sao_Mateus_do_Sul', 'Mafra', 'Iriniopolis', 'Papanduva']
variables_needed = ['umidade_relativa', 'vento', 'temperatura', 'balanço_hidrico']
all_things = nearby_city + variables_needed
extracted_status = {things: '' for variables_needed in all_things}
#extracted status
#Criando um dicionário para guardar o estado das cidades/variáveis utilizando um dict comprehension


list_Item_UmidadeRelativaSM = operation_column.find(class_="list-item-title list-item-expand").text
extracted_status['umidade_relativa'] = list_Item_UmidadeRelativaSM

variables_needed = operation_column.find_all(class_="list-variaveis-open")
for variables in variables_needed:
	variables_info_divs = variables.find_all(class_='radio-list list-item-content')
	for div in variables_info_divs:
		umidade_relativa:''
		vento:''
		temperatura: ''
		balanço_hidrico: ''
		extracted_status[umidade_relativa] = umidade_relativa_status
		extracted_status[vento] = vento_status
		extracted_status[temperatura] = temperatura_status
		extracted_status[balanço_hidrico] = balanço_hidrico_status
#extracted_status