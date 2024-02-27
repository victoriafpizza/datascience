# As exeções ão erros que ocoreem dentro a execução do programa e interrompem o fluxo do programa quando não tratadas
# Identificando erros e tratando eles

# TRY EXECPT 

# Se uma exceção for lançada, quebramos a execução de try e continuamos com o que recisa ser executado em
# except, que seria a clausula de exeção. Ou seja, a clausula except so ser aacionada se uma exceção for lançada  
# na clausula try

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
nome = input("Digite o nome do(a) estudante: ")
resultado = notas[nome]
resultado

try:
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except Exception as e:
    print(type(e), f"Erro: {e}")

