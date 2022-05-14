import pandas as pd                                                     # manipulação de dados
import matplotlib.pyplot as plt                                         # visualização de dados
import seaborn as sns                                                   # visualização de dados
from sklearn.feature_extraction.text import CountVectorizer             # machine learn (Cálculos)


def retornarDadosUnicos(listaValores, campo):
    list(listaValores)
    listaValores[campo] = listaValores[campo].str.lower().values
    semValoresNA = listaValores[campo].dropna()
    vetor = CountVectorizer(token_pattern='(?u)\\b[\\w-]+\\b', analyzer='word').fit(semValoresNA)
    dadoUnico = vetor.get_feature_names()
    dadoUnico = [d for d in dadoUnico if len(d) > 1]
    return dadoUnico


def retornarDadosUnicosInteiro(listavalores):
    listavalores = sorted(listavalores)
    primeiroNumero = listavalores[0]
    numerosAgrupados = []
    numerosAgrupados.append(primeiroNumero)
    for nm in listavalores:
        if primeiroNumero != nm:  # Evitando numeros iguais
            primeiroNumero = nm
            numerosAgrupados.append(primeiroNumero)
    return numerosAgrupados


dadosCompraJson = pd.read_json("jsonExercicio05/dados_compra.json")     # Dados Json

sexoUnico = retornarDadosUnicos(dadosCompraJson, 'Sexo')
idadeUnico = retornarDadosUnicosInteiro(dadosCompraJson['Idade'])
#print(sexoUnico)
#print(idadeUnico)
'''
# Criação do gráfico
plt.figure(figsize=(16, 8))
sns.barplot(y=sexoUnico, x=idadeUnico, orient='h')

# Loop com valores
for i in range(len(dadosCompraJson)):
    plt.text(dadosCompraJson[dadosCompraJson.index[i]],
             i + 0.25,
             round(dadosCompraJson['Idade'][dadosCompraJson.index[i]], 2))

plt.ylabel("Sexo")
plt.xlabel("\nIdade dos compradores")
plt.title("\nAnálise dos Consumidores\n")
plt.show()'''
