#! /usr/bin/env python3 
# -*- coding: utf-8 -*- 

## Importação dos módulos necessários para a análise de dados e visualização
import pandas as pd  # Para manipulação de dados
import numpy as np   # Para cálculos numéricos
from sklearn.linear_model import LinearRegression  # Para criar o modelo de regressão linear
import matplotlib.pyplot as plt  # Para plotar gráficos

## Carrega o dataset 'LungDisease.csv' (doença pulmonar) em um DataFrame do pandas
doenca_pulmao_csv = 'LungDisease.csv'
dataset_doenca_pulmao = pd.read_csv(doenca_pulmao_csv)

## Primeira visualização dos dados: plotando um gráfico de dispersão (scatter plot) 
## para ver a relação entre 'Exposure' (exposição) e 'PEFR' (taxa de fluxo expiratório)
dataset_doenca_pulmao.plot.scatter(x='Exposure', y='PEFR')
plt.show()  # Exibe o gráfico

## Definição das variáveis:
## 'preditoras' contém a variável independente ('Exposure')
## 'alvo' contém a variável dependente ('PEFR')
preditoras = ['Exposure']
alvo = 'PEFR'

## Criação do modelo de regressão linear simples
model = LinearRegression()
## Ajuste do modelo usando os dados do dataset
## O modelo será treinado para prever 'PEFR' com base em 'Exposure'
model.fit(dataset_doenca_pulmao[preditoras], dataset_doenca_pulmao[alvo])

## Exibição dos coeficientes obtidos pelo modelo ajustado
## Intercepto é o valor de 'PEFR' quando 'Exposure' é 0
## Coeficiente de exposição é o valor que multiplica a variável 'Exposure' na equação da reta
print(f'Intercepto: {model.intercept_:.3f}')
print(f'Coeficiente de exposição: {model.coef_[0]:.3f}')
print(f'Equação: Y = {model.intercept_:.3f} + {model.coef_[0]:.3f} X')

## Visualização gráfica da reta de regressão
fig, ax = plt.subplots()
## Definindo os limites dos eixos X e Y
ax.set_xlim(0, 23)  # Limites para 'Exposure'
ax.set_ylim(295, 450)  # Limites para 'PEFR'
## Definindo os rótulos dos eixos
ax.set_xlabel('Exposure')
ax.set_ylabel('PEFR')
## Desenhando a reta de regressão com base nos valores de 'Exposure' (0 a 23)
ax.plot((0, 23), model.predict(pd.DataFrame({'Exposure': [0, 23]})))
## Marcando o intercepto (b_0) no gráfico, que é onde a reta cruza o eixo Y
ax.text(0.4, model.intercept_, r'$b_0$', size='larger')

plt.show()  # Exibe o gráfico com a reta de regressão

## Cálculo dos erros do modelo (diferença entre os valores reais e os previstos)
previsto = model.predict(dataset_doenca_pulmao[preditoras])  # Valores previstos pelo modelo
erros = dataset_doenca_pulmao[alvo] - previsto  # Diferença entre os valores reais e os previstos

## Exibição dos valores reais, previstos e os erros para cada ponto de dados
for x, real, p, erro in zip(dataset_doenca_pulmao.Exposure,
                            dataset_doenca_pulmao.PEFR,
                            previsto,
                            erros):
    print(f"X: {x}  Valor real: {real}  Valor Previsto: {p}  Erro: {erro}")

## Visualização gráfica dos erros
## Primeiro, um gráfico de dispers
