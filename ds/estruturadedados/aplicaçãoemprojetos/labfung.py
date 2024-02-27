gabarito = ['D', 'A', 'B', 'C', 'A']

# Criando a função que recebe a lista de listas com as notas dos estudantes
def corretor(testes: list):
  pontuacoes = [] # criando a lista que receberá as pontuações caso a exceção não seja lançada
  try:
    for teste in testes:
      nota = 0 # variável que acumula a nota de cada estudante
      for i in range(len(teste)):
        if teste[i] not in ['A', 'B', 'C', 'D']: # Verificamos se temos uma alternativa valida
          raise ValueError(f'A alternativa {teste[i]} não é uma opção de alternativa válida')
        elif teste[i] == gabarito[i]: # Verificamos se as respostas são iguais e adicionamos à nota
          nota += 1
      pontuacoes.append(nota) # adicionamos a nota do(a) estudante na lista de pontuações
  except Exception as e:
    print(e)
  else:
    return pontuacoes # retornando a lista de pontuações se não lançarmos a exceção

# Testando no exemplo que não lança exceção
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
corretor(testes_sem_ex)

# Testando no exemplo que lança exceção
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
corretor(testes_com_ex)
