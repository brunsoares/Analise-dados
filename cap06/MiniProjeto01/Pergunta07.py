import numpy as np                                                      # manipulação de dados
import pandas as pd                                                     # manipulação de dados
import matplotlib.pyplot as plt                                         # visualização de dados
import seaborn as sns                                                   # visualização de dados
import Util

def Resposta07(connection):
    print("\nPergunta 07: \n")

    # AVG() função para pegar o valor medio na consulta SQL
    consultaPerg07 = '''
                     Select AVG(runtime_minutes) tempoMedio, genres
                     From titles
                     Where type = 'movie'
                     And runtime_minutes != 'NaN'
                     Group By genres
                     '''

    resultadoPerg07 = pd.read_sql_query(consultaPerg07, connection)

    generosUnicos = Util.retornarGeneros(resultadoPerg07)

    # Cálculo duração por genêro
    generoTempo = []
    for item in generosUnicos:
        consulta = "Select runtime_minutes tempo From titles where genres Like " + "\'" + "%" + item + "%" + "\' And type = \'movie\' And tempo != 'NaN'"
        resultado = pd.read_sql_query(consulta, connection)
        generoTempo.append(np.median(resultado['tempo']))

    # Preparando dataFrame
    dataFrameTempo = pd.DataFrame()
    dataFrameTempo['genres'] = generosUnicos
    dataFrameTempo['tempo'] = generoTempo

    dataFrameTempo = dataFrameTempo.drop(index=18)  # Drop no indice 18 (News)
    dataFrameTempo = dataFrameTempo.sort_values(by='tempo', ascending=False)  # Ordenando

    print(dataFrameTempo)

    # Criação do gráfico
    plt.figure(figsize=(16, 8))
    sns.barplot(y=dataFrameTempo.genres, x=dataFrameTempo.tempo, orient='h')

    # Loop com valores
    for i in range(len(dataFrameTempo.index)):
        plt.text(dataFrameTempo.tempo[dataFrameTempo.index[i]],
                 i + 0.25,
                 round(dataFrameTempo['tempo'][dataFrameTempo.index[i]], 2))

    plt.ylabel("Genêro")
    plt.xlabel("\nMediana de Tempo de Duração (Minutos)")
    plt.title("\nRelação Entre Duração e Genêro\n")
    plt.show()
