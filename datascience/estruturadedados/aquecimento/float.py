# 1. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números.
# O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.
# Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.

try:
    numero_1 = float(input())
    numero_2 = float(input())
    divisao = numero_1 / numero_2
except Exception as e:
    print(type(e), f'Erro: {e}')
