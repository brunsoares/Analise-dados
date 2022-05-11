import random

class Auxiliar:
    def __init__(self, palavra):
        self.palavra = palavra
        self.listaAcerto = []
        self.listaErro = []

    def checarLetra(self, letra):
        if letra in self.palavra and letra not in self.listaAcerto:
            self.listaAcerto.append(letra)
        elif letra not in self.palavra and letra not in self.listaErro:
            self.listaErro.append(letra)

    def checkStatus(self, letra):
        if letra in self.palavra:
            return True
        else:
            return False


#Lista com os desenhos do console
desenho = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    0   |
        |
        |
        |
    =========
    ''',
   '''
   +---+
   |   |
   0   |
   |   |
       |
       |
   =========
    ''',
    '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
    =========
    ''',
    '''
     +---+
     |   |
     0   |
    /|\  |
    /    |
         |
    =========
    ''',
    '''
     +---+
     |   |
     0   |
    /|\  |
    / \  |
         |
    =========
   '''
  ]

def printDesenho(indice):
    print(desenho[indice])

#Metodos fora da classe
def escolherPalavra():
    with open("palavras.txt", "rt") as linhas:
        valor = linhas.readlines()
    return valor[random.randint(0, len(valor))].strip()

def montarPalavra(palavra):
    listaPalavra = []
    for i in range(0, len(palavra)):
        listaPalavra.append("_")

    return listaPalavra

def adicionarLetra(palavra, letra, listaPalavra):
    listaLetras = list(palavra)
    indice = -1
    if letra != "" and letra in palavra:
        indice = listaLetras.index(letra)
    if indice != -1:
        listaPalavra[indice] = letra
    return listaPalavra

def tratarPalavra(palavra):
    palavraTxt = ""
    for lt in palavra:
        palavraTxt += (lt + " ")
    return palavraTxt

