#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score


## Parte principal do script - - - - - - - - - - - - - - - - - - - - -#
arquivo_csv = 'Social_Network_Ads.csv'
data_frame = pd.read_csv(arquivo_csv)

## exibe informações básica do data frame
print(data_frame.head(), end='\n\n')
print(data_frame.info(), end='\n\n')
print(data_frame.describe(), end='\n\n')

## removemos a coluna User ID pois ela não será usada na nossa
## análise
data_frame.drop(columns = ['User ID'], inplace=True)

## Análise exploratória dos dados - - - - - - - - - - - - - - - - - - #
## analisando a distribuição dos dados para todas as colunas
## do data frame
sns.histplot(data_frame['EstimatedSalary'], kde=True)
plt.show()

sns.histplot(data_frame['Purchased'], kde=True)
plt.show()

sns.histplot(data_frame['Age'], kde=True)
plt.show()

## faremos o processamento da coluna Gender transformando este
## campo não numérico em numérico
label_encoder = LabelEncoder()
label_encoder.fit(data_frame['Gender'])
## as duas linhas servem para ver como o label encoder fez a
## transformção das classes
## print(label_encoder.transform(data_frame['Gender'].unique()))
## print(label_encoder.inverse_transform([1,0]))
data_frame['Gender'] = label_encoder.transform(data_frame['Gender'])
## também poderia ter feito as operações de fit e transform usando
## apenas o método fit_transform
## data_frame['Gender'] = label_encoder.fit_transform(data_frame['Gender'])

sns.histplot(data_frame['Gender'], kde=True)
plt.show()

## análise multivariada
matriz_correlacao = data_frame.corr()
print(matriz_correlacao, end='\n\n')
sns.heatmap(matriz_correlacao)
plt.show()

## iremos remover a coluna Gender, pois ela tem baixa correlação
## com as demais variáveis
data_frame.drop(columns=['Gender'], inplace=True)

## Treinamento do modelo - - - - - - - - - - - - - - - - - - - - - - -#
## variáveis preditoras
X = data_frame[['Age', 'EstimatedSalary']]
## variável alvo
Y = data_frame['Purchased']

## faz a divisão dos dados de treinamento e de teste
X_train, X_test, Y_train, Y_test = train_test_split(X,
                                                    Y,
                                                    test_size=0.2,
                                                    random_state=42)
## fazendo as devidas transformações nos dados
escalonador = StandardScaler()
X_train = escalonador.fit_transform(X_train)
X_test = escalonador.transform(X_test)

## cria o modelo e faz o treinamento
modelo = tree.DecisionTreeClassifier(criterion='entropy',
                                     random_state = 0)
modelo.fit(X_train, Y_train)

## Fazendo algumas previsões - - - - - - - - - - - - - - - - - - - - -#
Y_previsto = modelo.predict(X_test)

## Avaliação do modelo - - - - - - - - - - - - - - - - - - - - - - - -#
print(f'Acurácia: {accuracy_score(Y_test, Y_previsto)}')
print(f'Relatório de classificação:\n'
      f'{classification_report(Y_test, Y_previsto)}')

matriz_confusao = confusion_matrix(Y_test, Y_previsto)
sns.heatmap(matriz_confusao,
            annot=True,
            fmt='d',
            cbar=False)
plt.show()

## curva precisão x recall
## primeiro vamos computar a probabilidade de uma observação/dado
## qualquer pertencer a uma classe
## neste exemplo, iremos calcular a probabilidade de uma pessoa
## pertencer a classe dos compradores ou não compradores
Y_previsto_prob = modelo.predict_proba(X_test)[:,1]
precisao, recall, _ = precision_recall_curve(Y_test,
                                                  Y_previsto_prob)
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(recall,
        precisao,
        label='Classificação da Árvore de Decisão')
ax.set_title('Cruva precisão x recall')
ax.set_xlabel('Recall')
ax.set_ylabel('Precisão')
plt.show()

## curva AUC/ROC
## a curva ROC representa a taxa de verdadeiro positivo (TPR) contra
## a taxa de falso negativo (FPR)
## TPR = verdadeiro positivo / (verdadeiro positivo + falso negativo)
## FPR = falso negativo / (falso negativo + verdadeiro negativo)
## AUC é uma medida de separabilidade
## um AUC alto indica que o modelo distingue bem entre instâncias
## positivas das negativas
fpr, tpr, _ = roc_curve(Y_test, Y_previsto_prob)
auc_escore = roc_auc_score(Y_test, Y_previsto_prob)

fig, ax = plt.subplots(figsize=(6,6,))
ax.plot(fpr,
        tpr,
        label='AUC='+str(auc_escore))
ax.set_title('Curva ROC')
ax.set_xlabel('Taxa de Falso Positivo')
ax.set_ylabel('Taxa de Verdadeiro Positivo')
plt.legend(loc=4)
plt.show()
