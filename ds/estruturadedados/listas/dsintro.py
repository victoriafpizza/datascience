def buscamenor(arr):
    menor = arr[0] #armazena o menor valor
    menor_indice = 0 #armazena o indice do menor valor
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i 
        return menor_indice
    
    def ordenacaoPorSelecao(arr): #ordenações em um array
        novoArr = []
        for i in range(len(arr)):
            menor = buscamenor(arr) #encontra o menor elemento do array 
            novoArr.append(arr.pop(menor))
        return novoArr