import sklearn
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers.experimental.preprocessing import RandomFlip
from tensorflow.keras.layers.experimental.preprocessing import RandomRotation
from tensorflow.keras.layers.experimental.preprocessing import RandomZoom
from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import Precision
from tensorflow.keras.metrics import Recall
import functionsUtil as fu      # Funções Uteis


tf.random.set_seed(4)  # Reproduzindo diversos resultados

# DataSet usado = https://www.kaggle.com/datasets/moltean/fruits?resource=download

pathDadosTreino = Path("dados/fruits-360_dataset/fruits-360/Training")
pathDadosTeste = Path("dados/fruits-360_dataset/fruits-360/Test")

# Pegando todos os conteúdos das pastas
imagensTreino = list(pathDadosTreino.glob("*/*"))
print(imagensTreino[925:936])   # Amostra de dados

imagensTreino = list(map(lambda x: str(x), imagensTreino))  # Filtrando apenas os caminhos das imagens
print(imagensTreino[925:936])

labelsTreino = list(map(lambda x: fu.extrairLabels(x), imagensTreino))     # Adicionando nome as imagens conforme a fruta
print(labelsTreino[840:846])

# Convertendo a string de nome para objeto número para I.A
encoder = LabelEncoder()
labelsTreino = encoder.fit_transform(labelsTreino)
print(labelsTreino[840:846])    # Visualizando labels
labelsTreino = tf.keras.utils.to_categorical(labelsTreino)
print(labelsTreino[840:846])

# Dividindo dados - Treino / Validação
treinoX, validoX, treinoY, validoY = train_test_split(imagensTreino, labelsTreino)

# Tratamento das imagens - 224 x 224
tamanhoImagem = 224
redimensionar = tf.keras.Sequential([tf.keras.layers.experimental.preprocessing.Resizing(tamanhoImagem, tamanhoImagem)])

# Criando objeto dataSet augmentation
dataAugmentation = tf.keras.Sequential([RandomFlip("horizontal"), RandomRotation(0.2), RandomZoom(height_factor=(-0.3, -0.2))])

# Preparando Dados
#Parametros
batchSize = 32
autotune = tf.data.experimental.AUTOTUNE

# Criando dataSet
dataSetTreino = fu.preparaDataSetTF(treinoX, treinoY, batchSize, autotune, redimensionar, dataAugmentation)
dataSetValidacao = fu.preparaDataSetTF(validoX, validoY, batchSize, autotune, redimensionar, dataAugmentation, train=False)

# Shape dos objetos - Treino
imagem, label = next(iter(dataSetTreino))
print("Dados treino")
print(imagem.shape)
print(label.shape)

# Shape dos objetos - Validacao
imagemValid , labelValid = next(iter(dataSetValidacao))
print("Dados validação")
print(imagemValid.shape)
print(labelValid.shape)

# Visualizando uma imagem
print(encoder.inverse_transform(np.argmax(label, axis=1))[0])   # Transformação inversa de número para string
plt.imshow((imagem[0].numpy()/255).reshape(224, 224, 3))
plt.show()


# Criação do Modelo
modeloPreTreinado = EfficientNetB3(input_shape=(224, 224, 3), include_top=False)    # Modelo já pré-treinado
# Adicionando camadas próprias ao modelo
modelo = tf.keras.Sequential([modeloPreTreinado,
                             tf.keras.layers.GlobalAveragePooling2D(),
                             tf.keras.layers.Dense(131, activation='softmax')])
print("Modelo:")
print(modelo.summary())     # Sumário do modelo

# Parametros
lr = 0.001
beta1 = 0.9
beta2 = 0.999
ep = 1e-07

# Compilando modelo
modelo.compile(optimizer=Adam(learning_rate=lr, beta_1=beta1, beta_2=beta2, epsilon=ep),
               loss='categorical_crossentropy',
               metrics=['accuracy', Precision(name='precision'), Recall(name='recall')])

# Treinando modelo

historico = modelo.fit(dataSetTreino,
                       steps_per_epoch=len(treinoX)//batchSize,
                       epochs=6,
                       validation_data=dataSetValidacao,
                       validation_steps=len(treinoY)//batchSize)

# Após treinado, não necessita mais do modeloPreTreinado
modelo.layers[0].trainable = False
# Salvando modelo / Checkpoint
checkpoint = tf.keras.callbacks.ModelCheckpoint("modelo/checkpointModelo.h5",
                                                verbose=1,
                                                save_best=True,
                                                save_weights_only=True)

earlyStop = tf.keras.callbacks.EarlyStopping(patience=4)
print("Modelo após treinado:")
print(modelo.summary())

# Treinando modelo
historicoComCallbacks = modelo.fit(dataSetTreino,
                                   steps_per_epoch=len(treinoX)//batchSize,
                                   epochs=6,
                                   validation_data=dataSetValidacao,
                                   validation_steps=len(treinoY)//batchSize,
                                   callbacks=[checkpoint, earlyStop])

# Avaliando modelo
modelo.layers[0].trainable = True
modelo.load_weights("modelo/checkpointModelo.h5")       # Carregando modelo

# Carregando e preparando os dados de teste
caminhoImagensTeste = list(pathDadosTeste.glob("*/*"))
imagensTeste = list(map(lambda x: str(x), caminhoImagensTeste))
labelsTeste = list(map(lambda x: fu.extrairLabels(x), imagensTeste))
labelsTeste = encoder.fit_transform(labelsTeste)
labelsTeste = tf.keras.utils.to_categorical(labelsTeste)

# Convertendo ao tensor
testeImagens = tf.convert_to_tensor(imagensTeste)
testeLabels = tf.convert_to_tensor(labelsTeste)

dataSetTeste = (tf.data.Dataset
                .from_tensor_slices((imagensTeste, labelsTeste))
                .map(fu.carregarImagens(imagensTeste, labelsTeste, teste=True))
                .batch(batchSize))

# Avaliando modelo
loss, accuracy, precision, recall = modelo.evaluate(dataSetTeste)
print(f"Accuracy: {accuracy} \n"
      f"Precision: {precision} \n"
      f"Recall: {recall}")


# Previsões com modelo
fu.avaliarPrevisao("images/imagem1.jpg", modelo, encoder)
fu.avaliarPrevisao("images/imagem2.jpg", modelo, encoder)
fu.avaliarPrevisao("images/imagem3.jpg", modelo, encoder)
fu.avaliarPrevisao("images/imagem4.jpg", modelo, encoder)
fu.avaliarPrevisao("images/imagem5.jpg", modelo, encoder)
