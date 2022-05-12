import pandas as pd                                                     # manipulação de dados
import matplotlib.pyplot as plt                                         # visualização de dados


# 1- Quais são as categorias de filmes mais comuns no IMDB?
def Resposta01(connection):
    print("\nPergunta 01: \n")
    consultaPerg01 = "Select type, count(*) as count From titles Group By type"  # Consulta sql
    resultadoPerg01 = pd.read_sql_query(consultaPerg01, connection)
    # print(resultadoPerg01)
    resultadoPerg01["percentual"] = (resultadoPerg01["count"] / resultadoPerg01["count"].sum()) * 100  # Calculo %
    # print("\n")
    # print(resultadoPerg01)

    # Filtrando para mostrar apenas 4 categorias
    resto = {}
    # Somatoria de todos os restantes, com percentual abaixo de 5
    resto["count"] = resultadoPerg01[resultadoPerg01["percentual"] < 5]["count"].sum()  # Somatoria COUNT
    resto["percentual"] = resultadoPerg01[resultadoPerg01["percentual"] < 5]["percentual"].sum()  # Somatoria PERCENTUAL
    resto["type"] = "outros"  # alterando type
    # print(resto)

    # Top 3 categorias filtradas
    resultadoPerg01 = resultadoPerg01[resultadoPerg01["percentual"] > 5]  # filtrando acima de 5 percentual
    resultadoPerg01 = resultadoPerg01.append(resto, ignore_index=True)  # adicionando outros ja filtrados
    resultadoPerg01 = resultadoPerg01.sort_values(by="count", ascending=False)  # ordenando pelo count
    print(resultadoPerg01.head())

    # Criando gráfico
    labels = [str(resultadoPerg01["type"][i]) + ' ' + '[' + str(round(resultadoPerg01["percentual"][i], 2)) + '%' + ']'
              for i in resultadoPerg01.index]
    f = plt.figure()  # Setando a figura

    # Gerando gráfico
    plt.pie(resultadoPerg01["count"], labeldistance=1, radius=3, wedgeprops=dict(width=1.2))
    plt.legend(labels=labels, loc="center", prop={"size": 12})
    plt.title("Distribuição de Títulos", loc="Center", fontdict={"fontsize": 20, "fontweight": 20})
    plt.show()
