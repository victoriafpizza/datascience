# Criamos uma lista da situação dosestuadntes em que que caso sua media sejamaior ou igual a 6, ele recebra o "aprovado"
# e caso contrario recebera o valor "reporvado"

# Geraremos as lista com:

# lista de tuplas com o nome dos estudantes e seus codigos
# Lista de liistas com as notas de cada estudante
# Lista com as medias de cada estudante
# Lista da situação dos estudantes de acordo com as medias
# Os dados que utilizaremos são os mesmo que geramos nas situações

nomes = [('Joao', 'J720'), ('Maria', 'M205'), ('Jose',' J731'), ('Claudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# gerando lista de situações
situacao = [resultado_if cond else resultado_else for item in lista]

# condição é: nossa media tem que ser maior ou igual a 6. Se o if for correto, vamos passar aprovado, caso contrario else
# "reprovado"

situacao = ['Aprovado' if media >= 6 else "Reprovado" for media in medias]
situacao

# gerando lista de listas 
# [expr for item in lista de listas]

cadastro = [x for x in [nomes, notas, medias]]

# O x vai ler nomes e passsar. Depois vai ler notas e passar. Por fim vai ler medias e passar. Com isso criamos uma lista
# de listas nesse formato. Leremos o cadastro 

