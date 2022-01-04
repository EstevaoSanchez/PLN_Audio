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

resenhas = pd.read_csv('/home/estevao/VSC_PROJECTS/PLN_audio/base_dados/resenhas_treinamento.csv',
						sep=";",
						encoding='latin1')
print(resenhas)

lista_textos = resenhas['text_pt']


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
				palavra_trat = palavra_trat.replace("ç","c")
				palavra_trat = palavra_trat.replace('""',"")
				palavra_trat = palavra_trat.rstrip()				
				palavra_sem_acento = unidecode(palavra_trat)
				nova_frase.append(stemmer.stem(palavra_sem_acento))
		textos_tratados.append(nova_frase)

	return textos_tratados


textos_tratados = tratamento_texto(lista_textos)

resenhas['Texto_tratado'] = textos_tratados

resenhas_tratadas = pd.DataFrame(resenhas)

#print(resenhas_tratadas)

resenhas_tratadas.to_csv('/home/estevao/VSC_PROJECTS/PLN_audio/base_dados/resenhas_tratadas.csv',sep=";")
