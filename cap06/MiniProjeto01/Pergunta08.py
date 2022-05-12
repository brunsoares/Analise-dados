import pycountry                                                        # dados de países
import pandas as pd                                                     # manipulação de dados
import matplotlib.pyplot as plt                                         # visualização de dados
import seaborn as sns                                                   # visualização de dados


def Resposta08(connection):
    print("\nPergunta 08: \n")

    consultaPerg08 = '''
                     Select region, Count(*) numerosFilmes
                     From akas
                     Join titles On akas.title_id = titles.title_id
                     Where region != \'None\'
                     And type = \'movie\'
                     Group By region
                     '''

    resultadoPerg08 = pd.read_sql_query(consultaPerg08, connection)

    print(resultadoPerg08.shape)  # Informa quantidade de (Linhas, Colunas)

    # Listas Auxiliares
    nomePais = []
    contagemFilmes = []

    for i in range(resultadoPerg08.shape[0]):  # Rodando por todas as linhas
        try:
            codigo = resultadoPerg08['region'].values[i]
            nomePais.append(pycountry.countries.get(alpha_2=codigo).name)  # Pegando codigo do pais e retornando o nome
            contagemFilmes.append(resultadoPerg08['numerosFilmes'].values[i])
        except:
            continue

    # Preparando dataFrame
    dataFramePaises = pd.DataFrame()
    dataFramePaises['Paises'] = nomePais
    dataFramePaises['QntFilmes'] = contagemFilmes

    dataFramePaises = dataFramePaises.sort_values(by='QntFilmes', ascending=False)
    print(dataFramePaises.head(20))  # Top 10 paises

    # Criando gráfico
    plt.figure(figsize=(20, 8))
    sns.barplot(y=dataFramePaises[:20].Paises, x=dataFramePaises[:20].QntFilmes, orient='h')  # Top 20
    # Loop com adição de valores
    for i in range(0, 20):
        plt.text(dataFramePaises.QntFilmes[dataFramePaises.index[i]] - 1,
                 i + 0.30,
                 round(dataFramePaises['QntFilmes'][dataFramePaises.index[i]], 2))

    # Labels
    plt.xlabel("País")
    plt.ylabel("\nNúmero de Filmes")
    plt.title("\nNúmero de Filmes Produzido por País\n")
    plt.show()
