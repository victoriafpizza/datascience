num = int(input("Digite um numero inteiro de 1 a 10:"))

# Gerando a função tabuada()

def tabuada(numero: int):
    print(f"Tabuada do {numero}:")
    for i in range(11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
tabuada(num)