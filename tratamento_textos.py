
import nltk
import os
import readline
from nltk import tokenize
from nltk import word_tokenize
from string import punctuation
from unidecode import unidecode
from nltk.stem import PorterStemmer
import pandas as pd
#nltk.download("all")
#nltk.download('stopwords')
#nltk.download('punkt')



lista_arquivos=[x for x in os.listdir('/home/estevao/VSC_PROJECTS/PLN_audio/arquivos_texto') if x.endswith(".csv")]


lista_todos_textos = []
for arquivo in lista_arquivos:
	texto_arquivo =[]
	with open (f"/home/estevao/VSC_PROJECTS/PLN_audio/arquivos_texto/{arquivo}","r",encoding='UTF-8') as arq:
		for line in arq:
			texto_arquivo.append(line)	
	lista_todos_textos.append(texto_arquivo)	


def tratamento_texto (lista):
	palavras_irrelevantes = nltk.corpus.stopwords.words("portuguese")	
	stemmer = PorterStemmer()
	token_espaco = tokenize.WhitespaceTokenizer()
	textos_tratados = []
	#criando lista de pontuação
	pontuacao = []
	for ponto in punctuation:
		pontuacao.append(ponto)
	pontuacao.append('\\n')
	palavras_remover = palavras_irrelevantes + pontuacao 
		
	for i in range(0,len(lista)):
		frase = str(lista[i]).lower()
		palavras_texto = word_tokenize(frase)
		nova_frase = []
		for palavra in palavras_texto:
			if palavra not in palavras_remover:
				palavra_trat = palavra.replace("'","")
				palavra_sem_acento = unidecode(palavra_trat)
				nova_frase.append(stemmer.stem(palavra_sem_acento))
		textos_tratados.append(nova_frase)

	return textos_tratados
  		
				
textos_tratados = tratamento_texto(lista_todos_textos)

with open("/home/estevao/VSC_PROJECTS/PLN_audio/base_dados/Textos_Tratados.csv","a") as arq:
	y=1
	for txt in textos_tratados:
		texto_completo = str(txt)
		w = str(y)
		arq.write(w + ";" + texto_completo + "\n")
		y = y+1


#txt_tratado.to_csv('/home/estevao/VSC_PROJECTS/PLN_audio/base_dados/Textos_Tratados.csv') 	


    	
  	


