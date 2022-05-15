import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import scipy.stats as status
import sklearn.datasets as dtset    # Sklearn tem dataSets proprios, permitindo alguns testes
from sklearn.linear_model import LinearRegression   # Progrssão Linear
from sklearn.model_selection import train_test_split    # Divisão dos dados, minimizando erros do modelo

dataSetBoston = dtset.load_boston()
#print(dataSetBoston.data.shape)     # Dimensões dos dados

# Convertendo para dataFrame
dataFrame = pd.DataFrame(dataSetBoston.data)
dataFrame.columns = dataSetBoston.feature_names     # Ajustando titulos colunas

#print(dataSetBoston.target)     # Variavel de preços das casas

dataFrame['PRICE'] = dataSetBoston.target   # Adicionando ao data frame
print(dataFrame.head(10))

# Criando váriaveis para machine learn
variaveis = dataFrame.drop('PRICE', axis=1)     # Todas as variaveis (caracteristicas da casa)
preco = dataFrame.PRICE

# Gráfico
plt.scatter(dataFrame.RM, preco)
plt.ylabel("Preço da Casa")
plt.xlabel("Média do Número de Quartos por Casa")
plt.title("Relação entre Número de Quartos e Preço")
plt.show()

# Machine Learn
modelo = LinearRegression()
modelo.fit(variaveis, preco)    # Treinando modelo

#print(modelo.predict(variaveis))    # Prevendo o preço de todas as casas, comparando com o dataFrame

plt.scatter(dataFrame.PRICE, modelo.predict(variaveis))
plt.ylabel("Preço Original")
plt.xlabel("Preço Previsto")
plt.title("Preço Original x Preço Previsto")
plt.show()

# Cálculando a taxa de erro do modelo (MSE - Mean Squared Error) / MSE alto não é bom predictor de machine learn
modeloMse = np.mean((dataFrame.PRICE - modelo.predict(variaveis)) ** 2)     # Média de erros pelos preços
print("Taxa de erro do modelo = ", modeloMse)

# Ajustando modelo para minimizar o risco
treinoX, testeX, treinoY, testeY = train_test_split(variaveis, dataFrame.PRICE, test_size=0.30, random_state=5)
print(f"Corpo das variaveis: \n{treinoX.shape}\n{testeX.shape}\n{treinoY.shape}\n{testeY.shape}")

# Criando novo modelo
modeloAtual = LinearRegression()
modeloAtual.fit(treinoX, treinoY)   # Usando dados de treino

# Gráfico final comparando preços das casas originais com preços previsto no novo modelo
plt.scatter(modeloAtual.predict(treinoX), modeloAtual.predict(treinoX) - treinoY, c='b', s=40, alpha=0.5)
plt.scatter(modeloAtual.predict(testeX), modeloAtual.predict(testeX) - testeY, c='g', s=40, alpha=0.5)
plt.hlines(y=0, xmax=50, xmin=0, colors='red')
plt.ylabel("Resíduos")
plt.title("Teste de Resíduo - Treino(azul), Teste(verde)")
plt.show()
