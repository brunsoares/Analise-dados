import pandas as pd                                                     # manipulação de dados
import matplotlib.pyplot as plt                                         # visualização de dados
import seaborn as sns                                                   # visualização de dados
from sklearn.feature_extraction.text import CountVectorizer             # machine learn (Cálculos)


def Resposta02(connection):
    print("\nPergunta 02: \n")
    consultaPerg02 = "Select genres, Count(*) From titles Where type = 'movie' Group By genres"
    resultadoPerg02 = pd.read_sql_query(consultaPerg02, connection)
    resultadoPerg02['genres'] = resultadoPerg02['genres'].str.lower().values  # Convertendo valores para minusculo
    valoresSemNA = resultadoPerg02['genres'].dropna()  # Removendo valores N/A

    padrao = "(?u)\\b[\\w-]+\\b"    # Expressão Regular
    vetor = CountVectorizer(token_pattern=padrao, analyzer='word').fit(
        valoresSemNA)  # Criando vetor para contagem precisa

    bagGeneros = vetor.transform(valoresSemNA)  # Armazenando os valores
    generosValores = vetor.get_feature_names()  # Pegando os valores do genero
    generos = pd.DataFrame(bagGeneros.todense(), columns=generosValores,
                           index=valoresSemNA.index)  # Criando um DataFrame de visualização
    # print(generos.info())
    generos = generos.drop(columns='n', axis=0)  # Drop na coluna N, criada errado
    generosPercentual = pd.Series(generos.sum()).sort_values(ascending=False) / generos.shape[0] * 100
    print(generosPercentual.head(10))  # Top 10 generos com %

    # Gerar gráfico
    plt.figure(figsize=(16, 8))
    sns.barplot(x=generosPercentual.values, y=generosPercentual.index, orient="h",
                palette="terrain")  # Criação do gráfico de barras
    plt.ylabel("Gênero")
    plt.xlabel("\nPercentual de Filmes (%)")
    plt.title("\nNúmero de Títulos por Gênero\n")
    plt.show()
