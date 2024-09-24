#As funçoes são sequencias de insftruções em que alplicamos uma tarefa que pode ser reproduzida ao longo do codigo.
# Lista de Built-In Functions

print()
type()
list()

notas = {'1 semestre': 8.5, '2 semestre': 9.5, '3 semestre': 7}

# calcular a media das notas em uma casa decimal 
# dividimos pela quantidade de valores
# criando variavel soma

soma = 0 

for nota in notas.values():
    soma += nota

# o retorno é 25.0

# usando a função sum que recebe um iteravel para somar os valores 
    

somatorio = sum(notas.values())

# depois da soma feita precisamos pegar o tamanho da lista 

qtd_notas = len(notas)

media = somatorio / qtd_notas
media = round(media, 1)