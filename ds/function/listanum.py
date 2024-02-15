# lista dos numeros 
numeros = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]

# função lambda que eleva o numero ao contrario
quadrado = lambda x: x**2

# usando a função map()
resultado = list(map(quadrado, numeros))
