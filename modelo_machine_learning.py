import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
from nltk import ngrams

resenhas_treino = pd.read_csv('/home/estevao/VSC_PROJECTS/PLN_audio/base_dados/resenhas_tratadas.csv',
                                sep=';',
                                encoding='latin1')

classificacao = resenhas_treino['sentiment'].replace(["neg","pos"],[-1,1])

resenhas_treino['Classificacao'] = classificacao


tfidf = TfidfVectorizer(lowercase=False, ngram_range=(1,2))

tfidf_treino = tfidf.fit_transform(resenhas_treino["Texto_tratado"])

treino, teste, classe_treino, classe_teste = train_test_split(tfidf_treino,
                                                              resenhas_treino.Classificacao,
                                                              random_state=42)
        
# print(treino.shape)
# print(teste.shape)
modelo = ExtraTreesClassifier()
modelo_2 = ExtraTreesClassifier()
modelo.fit(treino,classe_treino)
resultado = modelo.score(teste,classe_teste)
print('\nAcurácia: ',resultado)
sentimento_atribuido = modelo.predict(teste)


