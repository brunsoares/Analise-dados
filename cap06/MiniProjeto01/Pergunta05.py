import pandas as pd                                                     # manipulação de dados
import matplotlib.pyplot as plt                                         # visualização de dados
import Util

def Resposta05(connection):
    print("\nPergunta 05: \n")

    consultaPerg05 = "Select genres From titles"

    resultadoPerg05 = pd.read_sql_query(consultaPerg05, connection)

    # Filtrando generos e tratamento
    generosUnicos = Util.retornarGeneros(resultadoPerg05)

    generoCount = []
    for item in generosUnicos:
        consulta = "Select Count(*) Count From titles Where genres Like " + "\'" + "%" + item + "%" + "\' And type = \'movie\' And premiered <= 2022"
        resultado = pd.read_sql_query(consulta, connection)
        generoCount.append(resultado['Count'].values[0])

    # Preparando um dataFrame
    dataFrameGeneros = pd.DataFrame()
    dataFrameGeneros['genre'] = generosUnicos
    dataFrameGeneros['Count'] = generoCount

    # Cálculo dos top 10
    dataFrameGeneros = dataFrameGeneros[dataFrameGeneros['genre'] != 'n']
    dataFrameGeneros = dataFrameGeneros.sort_values(by='Count', ascending=False)
    topGeneros = dataFrameGeneros.head(10)['genre'].values

    print(topGeneros)

    # Criando gráfico
    plt.figure(figsize=(16, 8))

    # For para pegar cada dado de cada genero
    for item in topGeneros:
        consultaGrafico = "Select Count(*) numeroGenero, premiered ano From titles Where genres Like " + "\'" + "%" + item + "%" + "\' AND type=\'movie\' AND ano <=2022 GROUP BY ano"
        resultadoGrafico = pd.read_sql_query(consultaGrafico, connection)
        plt.plot(resultadoGrafico['ano'], resultadoGrafico['numeroGenero'])

    plt.xlabel("\nAno")
    plt.ylabel("Número de Filmes Avaliados")
    plt.title("\nNúmero de Filmes Avaliados Por Genêro em Relação ao Ano de Estréia\n")
    plt.legend(labels=topGeneros)
    plt.show()
