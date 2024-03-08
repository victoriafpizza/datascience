#  Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, 
# no qual o primeiro e segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.

def soma_listas(lista1, lista2):
    try:
        if len(lista1) == len(lista2):
            dados = [(lista1[i], lista2[i], lista1[i]+lista2[i]) for i in range(len(lista1))]
        else:
            raise IndexError('A quantidade de elementos em cada lista é diferente.')
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        return dados  
