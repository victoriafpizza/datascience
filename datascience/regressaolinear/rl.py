#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

## Importação dos módulos - - - - - - - - - - - - - - - - - - - - - - #
import pandas as pd
import numpy  as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


## carrega o dataset
doenca_pulmao_csv = 'LungDisease.csv'
dataset_doenca_pulmao = pd.read_csv(doenca_pulmao_csv)

## primeira visualização dos dados
dataset_doenca_pulmao.plot.scatter(x='Exposure', y='PEFR')
plt.show()

## seta as variáveis preditoras e avlo
preditoras = ['Exposure']
alvo = 'PEFR'

## criação do modelo usando regressão linear simples
model = LinearRegression()
model.fit(dataset_doenca_pulmao[preditoras],
          dataset_doenca_pulmao[alvo])

## exibe dos dados coeficientes calculados pelo método fit
print(f'Intercepto: {model.intercept_:.3f}')
print(f'Coeficiente de exposição: {model.coef_[0]:.3f}')
print(f'Equação: Y = {model.intercept_:.3f} + {model.coef_[0]:.3f} X')

## visualização da reta que representa a equação de regressão
fig, ax = plt.subplots()
## atribuição dos valores limites dos eixos x e y
ax.set_xlim(0, 23)
ax.set_ylim(295, 450)
## atribuição dos rótulos dos eixos x e y
ax.set_xlabel('Exposure')
ax.set_ylabel('PEFR')
## obtém os valores extremos da equação de regressão para desenhar os
## extremos da reta
ax.plot((0, 23), model.predict(pd.DataFrame({'Exposure': [0, 23]})))
## posiciona o intercepto (coeficiente b_0) na reta
ax.text(0.4, model.intercept_, r'$b_0$', size='larger')

plt.show()

## computa os erros do modelo
previsto = model.predict(dataset_doenca_pulmao[preditoras])
erros = dataset_doenca_pulmao[alvo] - previsto

for x, real, p, erro in zip(dataset_doenca_pulmao.Exposure,
                            dataset_doenca_pulmao.PEFR,
                            previsto,
                            erros):
    print(f"X: {x}  Valor real: {real}  Valor Previsto: {p}  Erro: {erro}")

## visualização gráfica dos erros
## dados do dataset
ax = dataset_doenca_pulmao.plot.scatter(x='Exposure', y='PEFR')
## dados previstos
ax.plot(dataset_doenca_pulmao.Exposure, previsto)

for x, y_real, y_previsto in zip(dataset_doenca_pulmao.Exposure,
                                 dataset_doenca_pulmao.PEFR,
                                 previsto):
    ax.plot((x,x), (y_real, y_previsto), '--', color='C1')

plt.show()
