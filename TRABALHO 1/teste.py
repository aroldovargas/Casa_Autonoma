import time
from random import randint

dicSP = {1:["SENSOR DE PRESENCA","Corredor",'1'],2:["SENSOR DE PRESENCA","Sala","1"]}
dicLA = {1:["LAMPADA","Sala",'desligada'],2:["LAMPADA","Corredor","desligada"]}



def verificaPresenca(dic):
	lst = []
	for chave in dic:
		#Significa que existem pessoas no ambiente
		if dic[chave][2] == "1":
			lst.append(dic[chave][1])

	return lst

def ligarLampada(dic,lst):
	for chave in dic:
		#Significa que a lampada esta em um ambiente com presenca logo deve ser ligada
		if dic[chave][1] in lst:
			dic[chave][2] = "ligada"
			
	return dic

lst = verificaPresenca(dicSP)
print(ligarLampada(dicLA,lst))


