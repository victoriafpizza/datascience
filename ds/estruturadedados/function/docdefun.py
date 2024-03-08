# É importante deixar o nosso codigo ou analise dos dados o mais acessivel para o publico
# Uma das formar de atingit esse proposito reside na documentação de funções. Auxiliando quem le o nosso projeto

# TYPE HINT 

# utilizado no python para indicar o tipo de dado esperado de um parametro ou retorno de função auxiliando na legibilidade
# e manutenção do codigo. Podemos dizer em poucas palavras, que ela é a dica de tipagem dos dados 

def media(lista: list) -> float:
    calculo = sum(lista) / len(lista)
    return calculo

# se escrevemos a função media() em outra e passarmos o mouse por cima, podemos observar a seguinte imagem apontando as dicas
# de tipagem dos parametros de entrada e retorno da função

# DEFAULT VALUE 

# No python, o Default é um valor padrão atribuido a um argumento de função que é utilizado caso nenhum veja 
# passado pelo usuário

# Implementando ainda mais a nossa função media(), podemos utilizar o default value da seguinte forma:

def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)
    return calculo

# DOCSTRING

# String literal usada para documentar modulo, função, classeou metodo em Python. Ela é colocada como o primeiro 
#  item de definição e pode ser acessada usando a função help(). Ele descreve proposito, paramettros, tipo de retorno e 
# exeções levantads pela função 

def media(lista: list=[0]) -> float: 
    
    ''' Função para calcular  media de notas passadas por uma lista
    lista: list, default [0]
    Lista com as notas para calcular a media
    return = calculo: float
    Media Calculada
    '''
    calculo = sum(lista) / len(lista)
    return calculo
