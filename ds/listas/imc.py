alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso/altura**2), 1) for altura, peso in zip(alturas, pesos)]
print(imc)

# Neste exemplo, utilizamos o lisrt comprehension para ler cada um dos valores das listas de altura e peso que foram 
# pareados no zip() e calculamos o IMC arredondando em uma cada decimal