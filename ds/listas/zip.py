# O zip receb uma ou mais iteraveis (lista, string, dict,) e retorna como um iterador de tuplas onde cada elemento dos 
# iteraveis são pareados

estudantes = zip(nomes, medias)
estudantes

# É UJMA FUNÇÃO EMB UTIDA DO PYTHON QUE RECEB UM OU MAIS ITERAVEIS. 
# pode ser usada com map e filter

objeto_zip = zip([1,2,3])
objeto_zip

list(objeto_zip)

id = [1, 2, 3, 4, 5]
regiao = ['Norte', 'Nordeste', 'Sudeste' 'Centro-Oeste', 'Sul']

mapa = list(zip(id, regiao))
mapa
