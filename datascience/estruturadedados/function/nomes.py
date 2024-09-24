nomes = ["joao", "Maria", "Jose"]
sobrenomes = ["SILVA", "Souza", "Tavares"]

nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()} , nomes, sobrenomes')

# leitura do objeto mapa (iteravel)

for i in nome_completo:
    print(f"Nome completo: {n}")