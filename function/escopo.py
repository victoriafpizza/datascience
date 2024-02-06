# Em python, o escopo de uma variavel é definido pela região do codigo onde ela p-ode ser acessada. No caso de uma função,
# o escopopode ser dividido em duas categorias: global e local.

# Escopo Global é o espaço no qual uma variavel pode ser acdessada por qualquer função ou codigo que esteja executado no 
# programa. 

# Ja no Escopo Local é o espaço no qual a variavel pode ser acsessada apenas pela função em que foi definida 

# O problema de escopo ocorre quando uma variavel é definida dentro do escopo de uma função e, em seguida, é referenciada 
# fora do escopço da função. Nesse caso, o Python gera uma mensagem de erro, indicando que a variavel não foi definida

NameError

# Abaixo segue um exemplo que ilustra esse comportamento. Inicialmente cdriando a variavel x externa a função soma()
# na qual definimos uma outra variavel y e por fim imprimimos a soma das duas variaveis

x = 7 

def soma():
    y = 9 
    print(x + y)
    
# O x é a nossa variavel definida no escopo global e o y a variavel definida no escopo local da função soma()
# Quando tentamos executar a nossa função, a soma é realizada normalmente
    
soma() # o console imprime 16

# No entanto, o Python gera um erro quando tentamos imprimir a soma nde x e y fora do escopo da função, pois a variavel y
# existe apenas dentro da função soma()

print(x + y) #y tem que virar uma variavel global ou retornar seu valor na função e atribuila a uma variavel externa.



