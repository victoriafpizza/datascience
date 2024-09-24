# Abrangencia de Dicionarios, usadno laços, condiccionais e expressões para construir dicionarios a
# partir do formato de uma unica linha usando essas expressões
# As cahves do nosso dicionario serão as colunas identificando o tipo de dado
# os valores serão as listas com os dados correspondentes aquela chave

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

coluna = ["Notas", "Media Final", "Situação"]
# cadastro  = {chave: valor for item in range(len(coluna))}

# Por fim,passaremos os valores que entrarão em chave e valor. Para chave, vão ser as colunas
# coluna[1] -> coluna na posição i

cadastro  = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))}
cadastro

cadastro["Estudante"] = [lista_completa[0][i][0]for item in range(len(lista_completa[0]))]


