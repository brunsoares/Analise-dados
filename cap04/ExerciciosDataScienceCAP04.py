#1-
print("Exercicio 1")
listaEx1 = [5, 10, 15]
listaEx1Print = list(map(lambda x: x**3, listaEx1))
print(listaEx1Print)
print("-*-"*30)

#2-
print("Exercicio 2")
palavras = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil'.split()
resultado = list(map(lambda lt: [lt.upper(), lt.lower(), len(lt)], palavras))
print(resultado)
print("*-*"*30)

#3-
print("Exercicio 3")
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
listaEx3Print = [[val1[0] for val1 in matrix], [val2[1] for val2 in matrix]]
print(listaEx3Print)
print("-*-"*30)

#4-
print("Exercicio 4")
listaEx4 = [0, 1, 2, 3, 4]
elevaQuadrado = lambda x: x**2
elevaCubo = lambda x: x**3
listaEx4Resultado = list(map(elevaQuadrado, listaEx4))
listaEx4Resultado.append(list(map(elevaCubo, listaEx4)))
print(listaEx4Resultado)
print("*-*"*30)

#5-
print("Exercicio 5")
listaA = [2, 3, 4]
listaB = [10, 11, 12]
listaEx5Resultado = list(map(lambda x, y: x**y, listaA, listaB))
print(listaEx5Resultado)
print("-*-"*30)

#6-
print("Exercicio 6")
listaEx6resultado = list(filter(lambda x: x < 0, range(-5, 5)))
print(listaEx6resultado)
print("*-*"*30)

#7-
print("Exercicio 7")
lista1 = [1, 2, 3, 5, 7, 9]
lista2 = [2, 3, 5, 6, 7, 8]
listaEx7Resultado = list(filter(lambda x: x in lista1, lista2))
print(listaEx7Resultado)
print("-*-"*30)

#8-
print("exercicio 8")
import time
hora = time.strftime("%d/%m/%Y %H:%M", time.localtime())
print(hora)
print("*-*"*30)

#9-
print("Exercicio 9")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 4, 'd': 5}
dict3 = {}
listaEx9Resultado = list(map(lambda x, y: dict3.setdefault(x, y), dict1.keys(), dict2.values()))
print(dict3)
print("-*-"*30)

#10-
print("Exercicio 10")
listaEx10 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
listaEx10Auxiliar = [y if x > 5 else '' for x, y in enumerate(listaEx10)]
listaEx10Resultado = list(filter(lambda x: x != '', listaEx10Auxiliar))
print(listaEx10Resultado)
print("-*-"*10, "Finalizado exercicios capitulo 4", "-*-"*10)
