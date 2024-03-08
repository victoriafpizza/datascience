# transformar ums lista com o nome e as notas dos tres trimestres de estudantes em uma lista simples com os nomes 
# separados das notas e uma lista de listas com as tres notas de cada estudante separadas umas das outras

notas_turma = ['Joao', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'Jose', 3.4, 7.0, 7.0, 'Claudia', 5.5, 6.6, 8.0 'Ana', 6.0, 10.0, 9.5]

# Temos uma lista de notas de turmas composta pelo nome do estudante, seguido das tres notas que tirou, são 5 estudantes e 15 notas. 

# consideramos joao como posição zero, como normalmente uma lista é referenciada. Então temos um padrão, 0, 4 e 8

nomes = []
notas_separadas = []

for i in range(len(notas_separadas)):
    if i % 4 == 0:
        nomes.append(notas_separadas[i])
    else:
        notas_turma.append(notas_separadas)

# precisamos agrupar os valores não de 1 em 1, mas de 3 em 3. 
# O metodo append sempre recebe apenas um valor colocado dentro de juma lista. Ela vai ser considerada um unico elemento 
        
notinhas = []

for i in range(0, len(notas_separadas), 3):
    notinhas.append([notas_separadas[i], notas_separadas[i+1], notas_separadas[i+2]])
notinhas

