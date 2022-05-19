import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import pickle


def correlacaoVariaveis(dados, size=10):
    correlacao = dados.corr()   # Função de correlação em formato de tabela
    fig, axies = plt.subplots(figsize=(size, size))
    axies.matshow(correlacao)
    plt.xticks(range(len(correlacao.columns)), correlacao.columns)
    plt.yticks(range(len(correlacao.columns)), correlacao.columns)
    plt.show()


# Carregando dados
dados = pd.read_csv("dataset/pima-data.csv")

print(dados.head(10))

correlacaoVariaveis(dados)

# Convertendo registros String [True/False] para númerico
diabetesRegistros = {True: 1, False: 0}
dados['diabetes'] = dados['diabetes'].map(diabetesRegistros)

# Distribuição dos registros
registrosTrue = len(dados.loc[dados['diabetes'] == True])
registrosFalse = len(dados.loc[dados['diabetes'] == False])
totalCasos = registrosTrue + registrosFalse
print("Número de casos verdadeiros: {0} ({1:2.2f}%)".format(registrosTrue, (registrosTrue / totalCasos) * 100))
print("Número de casos falsos: {0} ({1:2.2f}%)".format(registrosFalse, (registrosFalse / totalCasos) * 100))

# Separando registros TREINO / TESTE
variaveis = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']     # Principais variaveis
variavelTarget = ['diabetes']

eixoX = dados[variaveis].values
eixoY = dados[variavelTarget].values

dadosTeste = 0.30   # 30% teste / 70% treino
treinoX, testeX, treinoY, testeY = train_test_split(eixoX, eixoY, test_size=dadosTeste, random_state=42)

# Tratamento de dados Missing (nesse caso valores 0)
preencheMissing = SimpleImputer(missing_values=0, strategy='mean')  # Preenchendo com a media de cada coluna
treinoX = preencheMissing.fit_transform(treinoX)
testeX = preencheMissing.fit_transform(testeX)

# Treinando modelo
modeloPreditivo = GaussianNB()  # Algoritmo pronto dentro do Sklearn
modeloPreditivo.fit(treinoX, treinoY.ravel())   # Treinando modelo

# Exatidão no modelo nos dados de treino e teste
exatidaoTreino = modeloPreditivo.predict(treinoX)
print("Exatidão do Modelo (TREINO): {0:.4f}".format(metrics.accuracy_score(treinoY, exatidaoTreino)))
exatidaoTeste = modeloPreditivo.predict(testeX)
print("Exatidão do Modelo (TESTE): {0:.4f}".format(metrics.accuracy_score(testeY, exatidaoTeste)))

# Testando e salvando o modelo
filename = "modeloPrevisaoDiabetes.sav"
pickle.dump(modeloPreditivo, open("modelo/"+filename, 'wb'))

modeloCarregado = pickle.load(open("modelo/"+filename, 'rb'))
previsao1 = modeloCarregado.predict(testeX[17].reshape(1, -1))
previsao2 = modeloCarregado.predict(testeX[18].reshape(1, -1))
print("Previsões")
print(f"Previsão 1 = {previsao1}")
print(f"Previsão 2 = {previsao2}")
