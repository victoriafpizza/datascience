# a biblioteca random é responsavel por gerar numeros e sequencias aleatórias
import random 

estudantes = ["Joao", "Maria", "Jose", "Ana"]
estudantes2 = ["Joao", "Maria", "Jose"]


from random import choice #o metodo é o choice

#built-in function (função embutida) chamada help()
#help(choice) - esse comando explica pra que serve o import choice

estudante = choice(estudantes2)

