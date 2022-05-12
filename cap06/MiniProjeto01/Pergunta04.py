import numpy as np                                                      # manipulação de dados
import pandas as pd                                                     # manipulação de dados
import matplotlib.pyplot as plt                                         # visualização de dados


def Resposta04(connection):
    print("\nPergunta 04: \n")
    consultaPerg04 = '''
                 Select rating, premiered From ratings
                 Join titles On ratings.title_id = titles.title_id
                 Where premiered <= 2022 And type = 'movie'
                 Order By premiered
                 '''
    resultadoPerg04 = pd.read_sql_query(consultaPerg04, connection)
    # Cálculo da mediana ao longo dos anos
    avaliacoes = []
    for ano in set(resultadoPerg04['premiered']):
        avaliacoes.append(np.median(resultadoPerg04[resultadoPerg04['premiered'] == ano][
                                        'rating']))  # Vai adicionar caso o premiered for igual ao ano, calculando a mediana depois
    # Separando os anos
    anos = list(set(resultadoPerg04['premiered']))
    print("Anos -> ", anos[1:10])
    print("Avaliações -> ", avaliacoes[1:10])
    # Criação do gráfico
    plt.figure(figsize=(16, 8))
    plt.plot(anos, avaliacoes)
    plt.xlabel("\nAnos")
    plt.ylabel("Avaliação")
    plt.title("\nMediana de Avaliação dos Filmes em Relação ao Ano de Estréia \n")
    plt.show()

