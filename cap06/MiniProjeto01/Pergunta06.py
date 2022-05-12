import numpy as np                                                      # manipulação de dados
import pandas as pd                                                     # manipulação de dados


def Resposta06(connection):
    print("\nPergunta 06: \n")

    consultaPerg06 = '''
                     Select runtime_minutes tempo
                     From titles
                     Where type = 'movie' 
                     And tempo != 'NaN'
                     '''

    respostaPerg06 = pd.read_sql_query(consultaPerg06, connection)

    # Cálculo percentil
    for i in range(101):
        val = i
        perc = round(np.percentile(respostaPerg06['tempo'].values, i), 2)
        print(f"{i} percentil da duração é: {perc}")

    # Select para encontrar o filme com maior duração
    consultaMaiorDuracao = '''
                           Select runtime_minutes tempo, primary_title titulo
                           From titles
                           Where type = 'movie' 
                           And tempo != 'NaN'
                           Order By tempo Desc
                           Limit 1
                           '''

    resultadoMaiorDuracao = pd.read_sql_query(consultaMaiorDuracao, connection)

    print("\nFilme com maior duração:\n", resultadoMaiorDuracao)
