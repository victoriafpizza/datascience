# declarando a lista de notas

notas = []

for i in range(1,6):
    nota = float(input(f"Digite a {i} a nota"))
    notas.append(nota)

def media(lista):
    lista.remove(max(lista))
    lista.remove(min(lista))
    return sum(lista) / len(lista)

media = media(notas)
print(f"Nota de manobra: {round(media, 1)}")