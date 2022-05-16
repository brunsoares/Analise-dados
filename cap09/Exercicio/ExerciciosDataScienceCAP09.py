import time
import numpy as np
import pandas as pd
import matplotlib as mat
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

'''
    Extração e Tratamento dos dados
'''
print("-*-"*15+" Extração e Tratamento dos Dados "+"-*-"*15)
# Carregando dataSet
iris = load_iris()
dataFrame = pd.DataFrame(iris.data, columns=iris.feature_names)
print(f"Tamanho do dataSet = {len(dataFrame)}")
print(dataFrame.head(10))

print(iris.target_names)    # Categoria das plantas target(nomes)
print(iris.target)          # Categoria das plantas target

dataFrame['nomeEspecie'] = pd.Categorical.from_codes(iris.target, iris.target_names)    # Adicionando no DataFrame com valores diferentes ao dados já presentes
dataFrame['valoresTarget'] = iris.target
print(dataFrame.head(2))

# Extraindo os atributos
atributos = dataFrame.columns[:4]   # até a quarta coluna
print(atributos)

# Cálculo média das classes de plantas
print(dataFrame.groupby('valoresTarget').mean().T)

print("-*-"*45)
'''
    Exploração dos Dados
'''
print("-*-"*15+" Exploração dos dados "+"-*-"*15)
print(dataFrame.head(10))               # Antes da transposta
print(dataFrame.transpose(copy=True))   # Depois da transposta

print(dataFrame.info)   # Informações sobre dataFrame

print(dataFrame.describe())     # Resumo estatistico dos dados

print(dataFrame.isnull().sum(axis=0))   # Verificando se tem nulo
dataFrame.dropna()                      # Retirando valores null, caso tenha

print(dataFrame.count(axis=0))          # Contagem de registros

print("-*-"*45)
'''
    Plot dos gráficos
'''
print("-*-"*15+" Criação dos gráficos "+"-*-"*15)
dataFrame['sepal length (cm)'].hist()   # Histograma de uma coluna
plt.show()

eixoYSepalLength = dataFrame['sepal length (cm)'].values
eixoXTarget = dataFrame['valoresTarget'].values

m, b = np.polyfit(eixoXTarget, eixoYSepalLength,  1)
plt.plot(eixoXTarget, eixoYSepalLength, '.')
plt.plot(eixoXTarget, m*eixoXTarget + b, '-', color='red')
plt.ylabel("Sepal Length (cm)")
plt.xlabel("Número target")
plt.title("Relação Sepal Length x número target")
plt.show()

eixoYSepalLength = dataFrame['sepal length (cm)'].values
eixoXPetalLength = dataFrame['petal length (cm)'].values

m, b = np.polyfit(eixoXPetalLength, eixoYSepalLength,  1)
plt.plot(eixoXPetalLength, eixoYSepalLength, '.')
plt.plot(eixoXPetalLength, m*eixoXPetalLength + b, '-', color='red')
plt.ylabel("Sepal Length (cm)")
plt.xlabel("Petal Length (cm)")
plt.title("Relação Sepal Length x Petal Length")
plt.show()

pd.plotting.scatter_matrix(dataFrame, alpha=0.5, diagonal='hist', marker='.', range_padding=0.05)   # Scatter Matrix
plt.show()

dataFrame.hist()    # Todos os atributos em histograma
plt.show()



