import matplotlib.pyplot as plt                         # Visualização
from sklearn.linear_model import LinearRegression       # Machine Learn

# Para prever algo, precisamos dos dados passados, para ter como base
# Adicionando dados passados
diametro = [[7], [10], [15], [30], [45]]
precos = [[8], [11], [16], [38.5], [52]]

# Visualizando dados historicos
plt.xlabel("Diâmetro (cm)")
plt.ylabel("\nPreços (R$)")
plt.title("\nDiâmetro x Preços \n")
plt.plot(diametro, precos, 'k.')
plt.axes([0, 60, 0, 60])
plt.grid(True)
plt.show()

# Criando modelo de Machine Learn - Regressão Linear
modelo = LinearRegression()
modelo.fit(diametro, precos)    # Treinando modelo com dados
# Valores unicos do array 2D
#print(modelo.predict(np.array([20]).reshape(1, 1)))  # Reshape() serve para pegar valores unicos do array 2d
#print(modelo.predict([[20]]))
valorDiametro = int(input("Digite o tamanho da pizza (CM), para saber seu preço: "))
valor = modelo.predict([[valorDiametro]])   # Retorna [[xx]]
print("Com o tamanho {} cm, a pizza está saindo por R${:.2f}".format(valorDiametro, valor[0][0]))   # Pegando valor unico para formatar
