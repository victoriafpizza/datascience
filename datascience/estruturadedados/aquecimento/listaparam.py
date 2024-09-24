# Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. 
# Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.

def converte_lista(lista):
    try:
        nova_lista = [float(elemento) for elemento in lista]
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        return nova_lista
    finally:
        print('Fim da execução da função')
