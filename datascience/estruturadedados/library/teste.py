import numpy as np
from random import choice 
from random import randrange, sample

lista1 = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
lista = choice(lista1)

for i in range(0, 100):
    lista.append(randrange(100))

