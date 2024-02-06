from random import randrange, sample

lista = []

for i in range(0, 20):
    lista.append(randrange(100))

sample(lista, 5)