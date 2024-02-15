from random import randint

# As tuplas são usadas em python para guardar dados que não serão alterados, garantindo que não sejam alterados de 
# proposito ou acidentalmente 
# Para criar uma tupla basta colocar as informações entre parenteses. 

# cadastro = ('Julia', 23, 'Lucas', 15, 'São Paulo')

# Precisamos gerar uma lista de tuplas com os nomes dos estudantes e o codigo ID de cada um para a plataforma de analise de
# dados. A criação do codigo consiste em concatenar a primeira letra do nome do estudante a um numero aleatório de 0 a 999
# Os dados recebidos correspondem a uma lista dos nomes de cada estudante

estudantes = ["Joao", "Maria", "Jose", "Claudia", "Ana"]
estudantes

# prescisamos de uma lista de tuplas em que o primeiro elemento sera o nome do estudante e o codigo

def gera_codigo():
    return str(randint(0,999))

# Concatenando com os estudantes 

codigo_estudantes = []

for i in range (len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))
codigo_estudantes

# criamos uma lista de tuplas, cada tupla com o nome do estudante.