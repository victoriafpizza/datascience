# 5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. 
# Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. 
# Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.

# Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, 
# ocê deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". 
# O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. 
# Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.

# criando a função que recebe as duas listas e a operação a ser realizada
def divide_colunas(lista_1: list, lista_2: list) -> list:
  # try-except que verifica se é possível calcular a divisão e lança exceção se as listas tem tamanhos diferentes
  # ou se temos alguma divisão por zero em um dos cálculos entre os números das listas
  try:
    if len(lista_1) != len(lista_2): # Verificando se as listas tem o mesmo tamanho, se não lança uma exceção
      raise ValueError("As listas precisam ter o mesmo tamanho")

    # A função zip pareia os elementos das listas e uma lista é gerada por meio da razão entre os pares
    resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)] 
  except ValueError as e:
    print(e)
  except ZeroDivisionError as e:
    print(f"{e}: A 2ª lista não pode possuir um valor igual a 0")
  else:
    return resultado

# Testando no exemplo que não lança exceção
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)

# Testando no exemplo que lança exceção (ZeroDivisionError)
pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)

# Testando no exemplo que lança exceção (ValueError)
pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)
