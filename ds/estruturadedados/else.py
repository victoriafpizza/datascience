# ELSE
    
# O else, semelhante á if...else, pega o caso contrario. Ou seja, se não tiver uma execão, seguimos o fluxo do try.

# notas = {'João': [8.8, 9.0, 10.0], 'Maria: [9.0, 7.0, 6.0], 'Jose': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0], Ana': [6.8, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.8], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.8]}

try:
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except KeyError:
    print("Estudante não matriculado(a) na turma")
else:
    print(resultado)
