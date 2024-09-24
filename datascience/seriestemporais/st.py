#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal  import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima.model import ARIMA


## carregando os dados do arquivo csv
arquivo = "Electric_Production.csv"
data_frame = pd.read_csv(arquivo)

## altera o índice do data frame para que os dados
## sejam indexados por um interalo de tempo
data_frame.index = pd.to_datetime(data_frame.DATE,
                                  format="%m-%d-%Y")

## como usamos a coluna "DATE" para indexar as linha do
## data frame, então removemos esta coluna
data_frame.drop("DATE", axis=1, inplace=True)
# print(data_frame.head(), end='\n\n')

## gráfico do consumo do tempo x consumo de energia (Value)
plt.plot(data_frame.index, data_frame.Value)
plt.show()

## faz a descomposição da sérire temporal em: dados observados
## originalmente, tendência, sazonalidade e resíduo
decomposicao = seasonal_decompose(data_frame)
## plota um gráfico contendo os 4 dados da decomposição
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(15,8))
decomposicao.observed.plot(ax=ax1)
decomposicao.trend.plot(ax=ax2)
decomposicao.seasonal.plot(ax=ax3)
decomposicao.resid.plot(ax=ax4)
plt.tight_layout()
plt.show()


## aplicação do teste ADF
## obtém os dados da coluna Value para efetuarmos o teste ADF
X = data_frame.Value.values
ADF_resultado = adfuller(X)

print('Dickey-Fuller Aumentado')
print(f'Teste Estatístico: {ADF_resultado[0]:.4f}')
print(f'p-valor: {ADF_resultado[1]:.4f}')
print('Valores Críticos:')

for chave, valor in ADF_resultado[4].items():
    print(f'\t{chave}: {valor:.4f}')

print()

## transformação da série numa série estacionária
## aplica o log natural (base e) para transformar os valores
## do data frame (apenas na coluna Value)
df_log = np.log(data_frame)
## uma janela de tamanho 12 para calcular a média, ou seja,
## para cada linha do data frame, usa 12 valores para computar
## a média
ma_log = df_log.rolling(12).mean()
fig, ax = plt.subplots()
df_log.plot(ax=ax, legend=False)
ma_log.plot(ax=ax, legend=False, color='r')
plt.tight_layout()
plt.show()

## conclui o processo de transformação por subtrair os valores (da
## coluna Value) da média
df_sub = (df_log - ma_log).dropna()

## obtém os valores da média e desvio padrão para verificarmos
## visualmente se a série ficou estacionária após a transformação
ma_sub = df_sub.rolling(12).mean()
std_sub = df_sub.rolling(12).std()

fig, ax = plt.subplots()
df_sub.plot(ax=ax,  legend=False)
ma_sub.plot(ax=ax,  legend=False, color='r')
std_sub.plot(ax=ax, legend=False, color='g')
plt.tight_layout()
plt.show()

## vamos aplicar o teste ADF para verificar (de forma mais cientfíca)
## que a série ficou estacionária após as transformações
X_sub = df_sub.Value.values
ADF_resultado = adfuller(X_sub)

print('Dickey-Fuller Aumentado')
print(f'Teste Estatístico: {ADF_resultado[0]:.4f}')
print(f'p-valor: {ADF_resultado[1]:.10f}')
print('Valores Críticos:')

for chave, valor in ADF_resultado[4].items():
    print(f'\t{chave}: {valor:.4f}')

print()

## faremos a diferenciação para reduzir a variância, eliminar
## tendências a fim de de deixar a série com propriedades mais
## próximas de uma série estacionária e obter previsões mais precisas
## a diferenciação é calculada num período de tempo T de modo que
## valor em T = valor em T - valor em (T -1) (um período anterior)
df_diff = df_sub.diff(1)

## plotando o gráfico da série após a difrenciação
ma_diff = df_diff.rolling(12).mean()
std_diff = df_diff.rolling(12).std()
fig, ax = plt.subplots()
df_diff.plot(ax=ax, legend=False)
ma_diff.plot(ax=ax, legend=False, color='r')
std_diff.plot(ax=ax, legend=False, color='g')
plt.tight_layout()
plt.show()

## vamos aplicar o teste ADF novamente para analisarmos a série
## após a diferenciação
## precisamos usar o dropna para remover os valores nulos
## (oriundo dos cáculos feitos com as janelas), do contrário,
## iremos obter um erro envolvendo NAN's (NAN = not a number)
X_diff = df_diff.Value.dropna().values
ADF_resultado = adfuller(X_diff)

print('Dickey-Fuller Aumentado')
print(f'Teste Estatístico: {ADF_resultado[0]:.4f}')
print(f'p-valor: {ADF_resultado[1]:.10f}')
print('Valores Críticos:')

for chave, valor in ADF_resultado[4].items():
    print(f'\t{chave}: {valor:.4f}')

print()

## Agora estamos prontos para fazer previsões usando o ARIMA
## ARIMA = AutoRegressive Integrated Moving Average
lag_acf = acf(df_diff.dropna(), nlags=25)
lag_pacf = pacf(df_diff.dropna(), nlags=25)

## gráfico ACF
## esse gráfico serve para obtermos o valor de autoregression
## (primeiro valor que cruza o eixo x)
plt.plot(lag_acf)
plt.axhline(y=-1.96 / (np.sqrt((len(df_diff) - 1))),
            linestyle='--',
            color='gray',
            linewidth=0.7)
plt.axhline(y=0,
            linestyle='--',
            color='gray',
            linewidth=0.7)
plt.axhline(y=1.96 / (np.sqrt((len(df_diff) - 1))),
            linestyle='--',
            color='gray',
            linewidth=0.7)
plt.title("Autocorrelação")
plt.show()

## gráfico PACT
## esse gráfico serve para obtermos o valor da moving average
## (primeiro valor que cruza o eixo x)
plt.plot(lag_pacf)
plt.axhline(y=-1.96 / (np.sqrt((len(df_diff) - 1))),
            linestyle='--',
            color='gray',
            linewidth=0.7)
plt.axhline(y=0,
            linestyle='--',
            color='gray',
            linewidth=0.7)
plt.axhline(y=1.96 / (np.sqrt((len(df_diff) - 1))),
            linestyle='--',
            color='gray',
            linewidth=0.7)
plt.title("Autocorrelação Parcial")
plt.show()

## criação do modelo ARIMA
## df_log: é o data frame em que fizemos a primeira transformação,
##         que é a transformação usando o log,
##         note que este não é data frame em que fizemos a
##         diferenciação
## order=(2,1,2)
## 2: vem do gráfico acf
## 1: indica o número de diferenciações
## 2: vem do gráfico pacf
model = ARIMA(df_log, order=(2,1,2))
resultados_AR = model.fit()
# print(resultados_AR.summary())

## faz uma pequena previsão
previsoes = resultados_AR.forecast(steps=5)
print(previsoes)
