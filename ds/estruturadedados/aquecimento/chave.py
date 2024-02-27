# Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, armazenando o resultado do valor em uma variável. 
# O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.

try:
    chave = input()
    valor = idades[chave]
except KeyError:
    print('Nome não encontrado')
else:
    print(valor)
