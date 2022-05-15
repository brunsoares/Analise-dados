import numpy as np

#1-
print("Exercicio 1")
listNumpy = np.arange(0, 1000000)
listDuplicada = np.multiply(listNumpy, 2)
print(listDuplicada)
listNormal = []
for i in range(0, 1000000):
    num = i * 2
    listNormal.append(num)
#print(listNormal)
print("-*-"*30)

#2-
print("Exercicio 2")
listEx02 = np.arange(0, 10)
listEx02[5:9] = 0
print(listEx02)
print("-*-"*30)

#3-
print("Exercicio 3")
arrayEx03 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(arrayEx03[1])
print("-*-"*30)

#4-
print("Exercicio 4")
arrayEx04 = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
matrix = np.matrix(list(arrayEx04))
print(matrix)
print("Primera Linha - ", matrix[0])
print("Segunda Linha - ", matrix[1])
print("Segunda Coluna - ", matrix[0, 1], " ", matrix[1, 1])
print("Terceira Coluna - ", matrix[0, 2], " ", matrix[1, 2])
print("-*-"*30)

#5-
print("Exercicio 5")
arr = np.arange(15).reshape((3, 5))
print(arr)
transposta = np.transpose(arr)
print(transposta)
print("-*-"*30)

#6-
print("Exercicio 6")
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

for i, val in enumerate(cond):
    if val:
        print(xarr[i])
    else:
        print(yarr[i])
print("-*-"*30)

#7-
print("Exercicio 7")
arrayEx07 = np.array(np.arange(0, 10))
print(arrayEx07)
np.save("array.npy", arrayEx07)
arquivoAberto = np.load("array.npy")
print(arquivoAberto)
print("-*-"*30)

#8-
print("Exercicio 8")
import pandas as pd
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'a', 'b'])
print(obj.drop_duplicates())
print("-*-"*30)

#9-
print("Exercicio 9")
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
dados = resp.json()
dataFrameSite = pd.DataFrame(dados, columns=["number", "title", "labels", "state"])
print(dataFrameSite)
print("-*-"*30)

#10-
print("Exercicio 10")
import sqlite3
connect = sqlite3.connect("/database/imdb.db")
select = '''
         select t.primary_title, t.genres, r.rating  from titles t 
            join ratings r on r.title_id = t.title_id 
            where premiered= 2022 
                and t."type" = "movie"
                and r.rating >= 8
            order by r.rating desc
            limit 20;   
         '''
resposta = pd.read_sql_query(select, connect)

dataFrame = pd.DataFrame()
dataFrame['Nome'] = resposta['primary_title']
dataFrame['Genêro'] = resposta['genres']
dataFrame['Avaliação'] = resposta['rating']
print("Top 20 Filmes de 2022")
print(dataFrame)




