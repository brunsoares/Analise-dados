import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


# Extrair labels das imagens pelo caminho
def extrairLabels(path):
    return path.split("\\")[-2]


# Carrega e transforma as imagens
def carregarImagens(image, label, teste=False):
    image = tf.io.read_file(image)
    image = tf.io.decode_jpeg(image, channels=3)
    if teste:
        image = tf.image.resize(image, [224, 224], method='bilinear')
    return image, label


# Prepara dados para formato TensorFlow
def preparaDataSetTF(path, label, batchSize, autotune, redimensionar, dataAugmentation,  train=True):
    # Preparando dados e Criando dataSet
    caminhoImages = tf.convert_to_tensor(path)
    label = tf.convert_to_tensor(label)
    imagesDataSet = tf.data.Dataset.from_tensor_slices(caminhoImages)
    labelDataSet = tf.data.Dataset.from_tensor_slices(label)

    dataSet = tf.data.Dataset.zip((imagesDataSet, labelDataSet))
    dataSet = dataSet.map(lambda image, labels: carregarImagens(image, labels))
    dataSet = dataSet.map(lambda image, labels: (redimensionar(image), labels), num_parallel_calls=autotune)
    dataSet = dataSet.shuffle(1000)
    dataSet = dataSet.batch(batchSize)

    # Se for treino aplica o dataSet, caso contrario repete e retorna o mesmo
    if train:
        dataSet = dataSet.map(lambda image, labels: (dataAugmentation(image), labels), num_parallel_calls=autotune)

    dataSet = dataSet.repeat()

    return dataSet


# Carregar nova imagem para testes
def carregarNovaImagem(imagemPath):
    image = tf.io.read_file(imagemPath)
    image = tf.io.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [224, 224], method='bilinear')
    plt.imshow(image.numpy()/255)
    plt.show()
    image = tf.expand_dims(image, 0)
    return image


# Faz as previsões do modelo
def avaliarPrevisao(imagePath, model, encoder):
    image = carregarNovaImagem(imagePath)
    previsao = model.predict(image)
    pred = np.argmax(previsao, axis=1)  # Maior valor de probabilidade
    return encoder.inverse_transform(pred)[0]

