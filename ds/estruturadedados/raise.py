#  criar uma própria pensando em um comportamento que não queremos que ocorra em nosso programa. Para isso, usamos a palavra-chave raise que permitirá que lancemos uma exceção.


def media(lista: list=[0]) -> float:
    ''' Função para calcular a média de notas passadas por uma lista
    lista: list, default[0]
    Lista com as notas para calcular a média
    return calculo: float
    Média calculada 
    '''

# calculo sum(lista) / len(lista)

if len(lista) > 4:
    raise ValueError("A lista não pode possuir mais de 4 notas.")

try:
    notas = [6, 7, 8, 9, 8]
    resultado = media(notas)
except TypeError:
    print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
except ValueError as e:
    print(e)
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")