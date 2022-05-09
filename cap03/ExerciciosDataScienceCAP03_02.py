# 1-
print("Exercicio 1")
def numerosPares():
    lista = []
    for i in range(1, 21):
        if i % 2 == 0:
            lista.append(i)
    return lista
valores = numerosPares()
print(valores)
print("-*-"*30)

#2-
print("Exercicio 2")
def fraseMaiuscula(string):
    return print(str(string).upper())
fraseMaiuscula("Essa frase vai sair maiuscula!")
print("*-*"*30)

#3-
print("Exercicio 3")
def adicionar2(listaElementos):
    list(listaElementos)
    listaElementos.append(5)
    listaElementos.append(6)
    return listaElementos
listaElementos = [1,2,3,4]
print(adicionar2(listaElementos))
print("-*-"*30)

#4-
print("Exercicio 4")
def funcaoMultiplicacao(multiplicador, multiplicando=None):
    if multiplicando is None:
        multiplicando = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    else:
        list(multiplicando)
    int(multiplicador)
    valoresResultado = []
    for i in multiplicando:
        valoresResultado.append(i*multiplicador)
    return print(valoresResultado)
print("Apenas um parametro")
funcaoMultiplicacao(3)
print("Todos os parametros")
funcaoMultiplicacao(5, [2, 4, 6, 8, 10])
print("*-*"*30)

#5-
print("Exercicio 5")
#função anonima
somando = lambda numero1,numero2 : numero1+numero2
#equivalente a seguinte função
#def somando(numero1, numero2):
#    return numero1+numero2
resultado = somando(5, 10)
print(resultado)
print("-*-"*30)

#6-
print("Exercicio 6")
total = 0
def soma(argumento1, argumento2):
    total = argumento1 + argumento2
    print("Dentro da função o total é: ", total)
    return total
soma(10,40)
print("Fora da função o total é: ", total)
print("*-*"*30)

#7-
print("Exercicio 7")
celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = map(conversao := lambda valores: (valores*9/5)+32, celsius) #funcao lambda criada dentro de outra função
print(list(fahrenheit))
print("-*-"*30)

#8-
print("Exercicio 8")
dicionarioMetodos = {
    "Metodo 1": "SetDefault",
    "Metodo 2": "Pop",
    "Metodo 3": "Update",
    "Metodo 4": "Values",
    "Metodo 5": "Len",
    "Metodo 6": "Clear",
    "Metodo 7": "Copy",
    "Metodo 8": "FromKeys",
    "Metodo 9": "Get",
    "Metodo 10": "Items",
    "Metodo 11": "Keys",
    "Metodo 12": "PopItem"
}
print("Principais metodos de dicionario\n ", dicionarioMetodos)
print("*-*"*30)

#9-
print("Exercicio 9")
import pandas as pd
print("Principais metodos do pandas")
print(dir(pd))
print("-*-"*30)

#10-
print("Exercicio 10")
import openpyxl
fileName = "Analise mensal.xlsx"
def retornoEstatistico(file):
    dados = pd.read_excel(fileName)
    return dados.describe()
print(retornoEstatistico(fileName))



