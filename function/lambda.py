# Uma função lambda pode ser chamada de anonima, não precisa ser definida (sem nome)
# Media ponderada de notas de uma dada materia. Com as 3 notas (n1, n2, n3) do estudante e devolver a media ponderada

# Comparando uma função de qualitativo no formato de função para função anonima 
nota = float(input("Digite a nota do(a) estudante: "))

def qualitativo(x): 
    return x + 0.5

qualitativo(nota)

# Com lambda podemos passar como uma variavel

qualitativo(nota)

# Chamamos nossa função de lambda de mediap e ela recebe notas dde x, y e z, que terao um peso e divididas por 10

N1 = float(input("Digite a 1 nota do estudante:"))
N2 = float(input("Digite a 1 nota do estudante:"))
N3 = float(input("Digite a 1 nota do estudante:"))

mediap = lambda x, y, z: (x * 3 + y * 2 + z * 5) / 10
mediaestudante = mediap(N1, N2, N3)
mediap

print(f'O estudante atingiu a media de {mediaestudante}')

notasatualizadas = lambda x: x + qualitativo
notasatualizadas(mediaestudante)