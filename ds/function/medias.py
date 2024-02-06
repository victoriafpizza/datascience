# recebemos uma demanda de calcular a media de um estudande a partir de uma lista, sendo possivel alterar a quantiadde de 
# notas, sem impedir que o calculo seja refeito. Os dados recebidos, desta vez, correspondem a uma lista contendo apenas as 
# notas de um estudante de uma dada materia 

# notas do estudante
notas = [8.5, 9.0, 6.0, 10.0]

# para calcular a media, podemos utilizar os mesmos conceitos usados anteriormente. 
# utilkizamos os mesmos conceitos usados anteriormente com uma função media e um parametro chamado de lista 

def media(lista):
    calculo = sum(lista) / len(lista)
    print(calculo)

# A variavel calculo faz uma soma entre os itens da lista e divide o resultado pela quantiade de valores 

media(notas)
resultado = media(notas)

# Obteremos o NoneType como retorno, como se fosse nulo. Acontece por causa do escopo da função, que determina que uma 
# variavel que nasce dentro de uma função, tambem morre dentro desta. Existe apenas dentro da função, então não conseguiu
# utilizar esse valor