import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict


dataset = pd.read_csv('C:\DataLoad\Tweets_Mg.csv',encoding='utf-8')
tweets = dataset['Text'].values
classes = dataset['Classificacao'].values

# Objeto do tipo CountVectorizer.
vectorizer = CountVectorizer(analyzer="word")

# Usando o vectorizer para calcular a frequência de todas as palavras da lista de tweets
freq_tweets = vectorizer.fit_transform(tweets)

# Usando o algoritmo de classificação Naive Bayes Multinomial
modelo = MultinomialNB()

# Realizando o Treinamento com as Frequências e as Classificações
modelo.fit(freq_tweets,classes)


# Realizando o Treinamento de teste
# testes = ['Esse governo está no início, vamos ver o que vai dar',
#          'Estou muito feliz com o governo de Minas esse ano',
#          'O estado de Minas Gerais decretou calamidade financeira!!!',
#          'A segurança desse país está deixando a desejar',
#          'O governador de Minas é do PT',
#          'a ducação esta maravilhosa']


# freq_testes = vectorizer.transform(testes)
# modelo.predict(freq_testes)
# print(modelo.predict(freq_testes))

# Realizando a Técnica de Cross Validation para validar o treinamento
resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

# Medindo a Pontaria do Cross Validation
# Acurácia, basicamente é o percentual de acertos que modelo teve
print(metrics.accuracy_score(classes,resultados))

# Medidas de validação do modelo
# sentimento=['Positivo','Negativo','Neutro']
# print (metrics.classification_report(classes,resultados,sentimento))

# Matriz de confusão
# print(pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True))


# Bigrams
vectorizer = CountVectorizer(ngram_range=(1,2))
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)

resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)
print(metrics.accuracy_score(classes,resultados))
