import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def modeloLinear():
    # Criando modelo com Keras
    modelo = keras.Sequential([layers.Dense(1, use_bias=True, input_shape=(1,), name='layer')])
    # Otimizando o modelo
    otimizador = tf.keras.optimizers.Adam(learning_rate=0.01, beta_1=0.9, beta_2=0.99, epsilon=1e-05, amsgrad=False, name='Adam')
    # Adicionando ao modelo e preparando o mesmo
    '''
        MAE = Mean Absolute Error
        MSE = Mean Squared Error
    '''
    modelo.compile(loss='mse', optimizer=otimizador, metrics=['mae', 'mse'])
    return modelo


# Pegando dataSet público
# Detalhes sobre o dataset = "cs.toronto.edu/~delve/data/boston/bostonDetail.html"
dataSet = keras.utils.get_file("housing.data", "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data")
# Data set sem colunas, adicionando manualmente
nomeColunas = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
               'DIS', 'RAD', 'TAX', 'PTRATION', 'B', 'LSTAT', 'MEDV']

# Carregando dados csv personalizado
dados = pd.read_csv(dataSet,                # Caminho do dataSet
                    names=nomeColunas,      # Nome das colunas
                    na_values='N/A',        # Dados em N/A
                    comment='\t',           # Comentários sendo tab
                    sep=' ',                # Separador pelo Space
                    skipinitialspace=True)  # Pula o primeiro espaço

print(dados.head(10))

# Dividindo os dados para TREINO e TESTES   (80/20)
dadosTreino = dados.sample(frac=0.8, random_state=0)    # Randomizando amostras (80)
dadosTeste = dados.drop((dadosTreino.index))            # Restante dos dados (20)

# Regressão Linear Simples
# Gráfico de relação das variáveis MEDV e RM
fig, ax = plt.subplots()
eixoX = dadosTreino['RM']
eixoY = dadosTreino['MEDV']
ax.scatter(eixoX, eixoY, edgecolors=(0, 0, 0))
ax.set_xlabel("RM")
ax.set_ylabel("MEDV")
plt.show()

# Divisão dos valores Treino e Teste com eixos X e Y
treinoX = dadosTreino['RM']
treinoY = dadosTreino['MEDV']
testeX = dadosTeste['RM']
testeY = dadosTeste['MEDV']

# Pegando o modelo
modelo = modeloLinear()
# Gerando plot do modelo
tf.keras.utils.plot_model(modelo, to_file="images/modelo.png", show_shapes=True, show_layer_names=True,
                          rankdir='TB', expand_nested=False, dpi=100)

# Criação de Hiperparametros
nEpochs = 4000
batch_size = 256
nIdleEpochs = 100
nEpochLog = 200
nSampleSave = nEpochLog * treinoX.shape[0]
print(f"Checkpoint salvo a cada {nSampleSave} amostras")

# Callback criado
callbackEarlyStopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=nIdleEpochs, min_delta=0.001)
caminhoCheckpoint = "dados/"    # Caminho para salvar os dados

# Checkpoint callback, salvando o modelo durante tempos
checkpointCallback = tf.keras.callbacks.ModelCheckpoint(filepath='dados/', verbose=1, save_weights_only=True, save_freq=nSampleSave)
modelo.save_weights(caminhoCheckpoint.format(epoch=0))

# Treinamento
dadosHistoricos = modelo.fit(treinoX, treinoY, batch_size=batch_size, epochs=nEpochs, validation_split=0.1, verbose=1, callbacks=[callbackEarlyStopping, checkpointCallback])

# Métricas usadas no treinamento
print(f"Métricas = {dadosHistoricos.history.keys()}")
mse = np.asarray(dadosHistoricos.history['mse'])
val_mse = np.asarray(dadosHistoricos.history['val_mse'])

# Valores dataFrame
valoresN = len(mse)
valores = np.zeros((valoresN, 2), dtype=float)
valores[:, 0] = mse
valores[:, 1] = val_mse

# Criando dataFrame
passos = pd.RangeIndex(start=0, stop=valoresN)
dataFrame = pd.DataFrame(valores, passos, columns=['MSE de Treino', 'MSE de Validação'])
print(dataFrame.head())

# Gráfico
sns.set(style='whitegrid')
sns.lineplot(data=dataFrame, palette='tab10', linewidth=2.5)
plt.show()

# Resultado de Previsões
previsoes = modelo.predict(testeX).flatten()
print(f"Previsões do Modelo: \n{previsoes}")
