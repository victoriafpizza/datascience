import numpy as np
import time

# cria uma lista com 1000000 elementos
lista = list(range(1000000))

# transforma a lista em um array Numpy
array = np.array(lista)

# começa a cronometrar o tempo para a operação com a lista
start_time = time.time()

# realiza a operação de elevar ao quadrado cada elemento da lista
lista_quadrado = [i**2 for i in lista]

# para o cronômetro
list_time = time.time() - start_time

# começa a cronometrar o tempo para a operação com o array
start_time = time.time()

# realiza a operação de elevar ao quadrado cada elemento do array
array_quadrado = array**2

# para o cronômetro
array_time = time.time() - start_time

print("Tempo da operação com a lista: ", list_time)
print("Tempo da operação com o array: ", array_time)
