#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import statsmodels.api as sm
from scipy import stats


## Script principal - - - - - - - - - - - - - - - - - - - - - - - - - #
## carregando o dataset
arquivo_csv = "insurance.csv"
data_frame = pd.read_csv(arquivo_csv)

## fazendo o processamento das variáveis categóricas
label_encoder = LabelEncoder()

## para cada coluna categórica, faz a devida transformação em dados
## numéricos usando o LabelEncoder
for coluna in data_frame.select_dtypes(include='object').columns:
    if coluna != 'region':
        label_encoder.fit(data_frame[coluna])
        data_frame[coluna] = label_encoder.transform(data_frame[coluna])
    else:
        ## o parâmetro sparce_output diz que a matriz, retornada pelo
        ## encoder, não é esparsa (versão não compacta)
        one_hot_encoder = OneHotEncoder(sparse_output=False)
        ## é necessário fazer data_frame.loc[:, coluna:coluna] pois o
        ## enconder exibe uma matriz/data frame, ao invés de uma série
        colunas_codificadas = one_hot_encoder.fit_transform(data_frame.loc[:, coluna:coluna])
        ## o método get_featured_names_out, do one hot enconder, retorna
        ## os nomes das colunas resultantes do processo de fit
        ## deve ser fornecido uma lista com os nomes das colunas
        df_colunas_transformadas = pd.DataFrame(colunas_codificadas,
                                                columns=one_hot_encoder.get_feature_names_out([coluna]))
        df_codificado = pd.concat([data_frame, df_colunas_transformadas], axis=1)
        df_codificado.drop([coluna], axis=1, inplace=True)
        data_frame = df_codificado


## construção do modelo
## seleção das variáveis
## executar o modelo com:
## todas as variáveis, remover região, remover região e sexo
# var_preditoras = data_frame.drop(['charges', 'region'], axis=1)
var_preditoras = data_frame.drop(['charges', 'sex'], axis=1)
var_alvo = data_frame['charges']

## separação dos dados de treinamento e teste
## usando: 80% para treinameto e 20% para teste
x_train, x_test, y_train, y_test = train_test_split(var_preditoras,
                                                    var_alvo,
                                                    test_size=0.2,
                                                    random_state=0)
## treinamento do modelo
modelo_reg_multi = LinearRegression()
modelo_reg_multi.fit(x_train, y_train)

## avaliação do modelo
## imprime os coeficientes do modelo
print(f"Intercepto: {modelo_reg_multi.intercept_}")
coeficientes = pd.DataFrame(modelo_reg_multi.coef_,
                            var_preditoras.columns,
                            columns=['Coeficiente'])
print(f"Colunas: {coeficientes}\n")

## mostra o coeficiente de determinação
## (o quanto o modelo se ajusta aos dados)
# previsao = modelo_reg_multi.predict(var_preditoras)
previsao = modelo_reg_multi.predict(x_test)
# r_sq = modelo_reg_multi.score(var_alvo, var_preditoras)
r_sq = metrics.r2_score(y_test, previsao)
print(f"Coeficiente de Determinação (R^2): {r_sq}")
## cálculo do R^2 ajusado (penaliza variáveis não explicativas)
n = len(y_test)
k = x_test.shape[1]
adjusted_r_squared = 1 - (1 - r_sq) * (n - 1) / (n - k - 1)
print(f"R^2 ajustado: {adjusted_r_squared}")

## calculo dos erros
y_predicao = modelo_reg_multi.predict(x_test)
print('MAE:', metrics.mean_absolute_error(y_test, y_predicao))
print('MSE:', metrics.mean_squared_error(y_test, y_predicao))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_predicao)))

plt.scatter(previsao, y_test)
plt.xlabel("Valor previsto")
plt.ylabel("Valor real")
plt.title("Gráfico de dispersão: valor previsto x valor real")
plt.show()

## cáculo dos p-valores para verificar quais variáveis podem
## ser removidas do modelo
## de acordo com os p-valores, poderíamos remover as colunas
## sex e region
var_preditoras2 = sm.add_constant(data_frame.drop(['charges'], axis=1))
estimacao = sm.OLS(data_frame['charges'], var_preditoras2)
estimacao_pvalor = estimacao.fit()
print(estimacao_pvalor.summary())
