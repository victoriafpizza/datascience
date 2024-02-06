# Funções que retirnam valores, precisa da palavra - chave return ao final 

notas1 = [8.5, 9.0, 6.0, 10.0]

# pedindo return 

def media(lista):
    calculo = sum(lista) / len(lista)
    return calculo

# Apos executamos a criação, criaremos uma variavel resultado na qual salvaremos a media das notas

resultado = media(lista)

# SITUAÇÃO 3 

# Recebemos uma nmova demanda, desta vez, de calcular a media de um estudante a partir de uma lista e retornar tanto a media
# quanto a situação do estudante APROVADO, ou RESULTADO. 
 
notas2 = [6.0, 7.0, 9.0, 5.0]

# Agora vamos fazer a função do calculo, semelhante a anterior, e com algumas incrementações

def boletim(lista):
    media = sum(lista) / len(lista)

    if media >= 6:
        situacao = "aprovado"
    else:
        situacao = "reprovado"
    
    return (media, situacao)

boletim(notas2)

#a tupla pode ter valores diferentes tipos, ja que neste caso temos um numero float e uma string

media, situacao = boletim(notas2)

# criando um texto 

print(f'o (A) estudante atingiu uma media de {media} e foi {situacao}')