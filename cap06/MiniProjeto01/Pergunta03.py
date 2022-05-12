import numpy as np                                                      # manipulação de dados
import pandas as pd                                                     # manipulação de dados
import matplotlib.pyplot as plt                                         # visualização de dados
import seaborn as sns                                                   # visualização de dados
import Util


def Resposta03(connection):
    print("\nPergunta 03: \n")
    consultaPerg03 = '''
                     Select rating, genres From ratings
                     Join titles On ratings.title_id = titles.title_id
                     Where premiered <= 2022 And type = 'movie'
                     '''
    resultadopPerg03 = pd.read_sql_query(consultaPerg03, connection)

    generosUnicos = Util.retornarGeneros(resultadopPerg03)

    # Listas vazias para incrementar
    generoContador = []
    generoAvaliacao = []

    # Loop com consulta SQL
    for item in generosUnicos:
        # Lista de Contador
        consulta = 'Select Count(rating) From ratings Join titles On ratings.title_id = titles.title_id Where genres Like ' + '\'' + '%' + item + '%' + '\'' +' And type = \'movie\' '
        retorno = pd.read_sql_query(consulta, connection)
        generoContador.append(retorno.values[0][0])     # Adicionando a lista, os primeiros valores

        # Lista de avaliação
        consulta = 'Select rating From ratings Join titles On ratings.title_id = titles.title_id Where genres Like ' + '\'' + '%' + item + '%' + '\'' +' And type = \'movie\' '
        retorno = pd.read_sql_query(consulta, connection)
        generoAvaliacao.append(np.median(retorno['rating']))

    # Criando um data frame
    dataFrameGeneros = pd.DataFrame()
    dataFrameGeneros['genres'] = generosUnicos
    dataFrameGeneros['count'] = generoContador
    dataFrameGeneros['rating'] = generoAvaliacao

    #print(dataFrameGeneros.head(20))

    # Removendo indice 18 noticias (news)
    dataFrameGeneros = dataFrameGeneros.drop(index=18)
    dataFrameGeneros = dataFrameGeneros.sort_values(by='rating', ascending=False)   # Ordenando

    print(dataFrameGeneros.head(20))

    # Criando gráfico
    plt.figure(figsize=(16, 10))
    # Barras
    sns.barplot(y=dataFrameGeneros.genres, x=dataFrameGeneros.rating, orient="h")

    # Informações do Gráfico
    for i in range(len(dataFrameGeneros.index)):    # Até o final da lista
        plt.text(4.0,
                 i+0.25,
                 str(dataFrameGeneros['count'][dataFrameGeneros.index[i]]) + " filmes")    # Texto Contador

        plt.text(dataFrameGeneros.rating[dataFrameGeneros.index[i]],
                 i+0.25,
                 round(dataFrameGeneros['rating'][dataFrameGeneros.index[i]],
                 2))    # Texto Avaliação

    plt.ylabel("Genêro")
    plt.xlabel("Avaliação")
    plt.title("\nMediana de Avaliação por Genêro")
    plt.show()
