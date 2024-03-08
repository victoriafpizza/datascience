# Funções sem Parametros
#def é a palavra cahve para criar funções

def media():
    calculo = (10 + 9 + 8) / 3
    print(calculo)

media()

# funções com parametros 
# são as funções com dados que elas devem trabalhar

# coletando dados

nota1 = int(input("Digite sua media"))
nota2 = int(input("Digite sua media"))
nota3 = int(input("Digite sua media"))

def medinha(nota1, nota2, nota3):
    calculo = (nota1 + nota2 + nota3) / 3
    print(calculo)

medinha()

# os valores que passamos para a função são chamados de argumentos 
# O argumento não precisa ser necessariamente ser igual ao do parametro