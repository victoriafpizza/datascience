# Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua líder requisitou que você criasse um trecho de código que 
# recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT.

# Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. 
# Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado o uso de uma pontuação por meio da frase 
# "O texto apresenta pontuações na palavra "[palavra]".". 
# Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial.

# criando a função que recebe a lista de palavras
def avalia_texto(texto: list):
    for palavra in texto:
        if ',' in palavra or '.' in palavra or '!' in palavra or '?' in palavra:
            raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}".')
    return "Texto já tratado!" # retornando a verificação se não lançada a exceção 

# Testando no exemplo que não lança exceção
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

try:
  avaliacao = avalia_texto(lista_tratada)
except Exception as e:
  print(e)
else:
  print(avaliacao)

# Testando no exemplo que lança exceção
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

try:
  avaliacao = avalia_texto(lista_nao_tratada)
except Exception as e:
  print(e)
else:
  print(avaliacao)
