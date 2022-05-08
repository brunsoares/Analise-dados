#Capitulo 2
#1-
print("Exercicio 1")
lista = []
for i in range(1,11):
    lista.append(i)
    print(i)
print(lista)

print("-*-"*30)

#2-
print("Exercicio 2")
objetos = ['Bola', 'Skate', 'Mochila', 'Notebook', 'Livro']
print(objetos)

print("*-*"*30)

#3-
print("Exercicio 3")
nome = "Bruno"
sobreNome = "Soares"
print(f"Hello World, meu nome é {nome} {sobreNome}, eh isso!")

print("-*-"*30)

#4-
print("Exercicio 4")
tuplaValor = (1, 2, 2, 3, 4, 4, 4, 5)
print(f"A quantidade de 4 que aparece é igual a {tuplaValor.count(4)}")

print("*-*"*30)

#5-
print("Exercicio 5")
dicVazio = {}
print(dicVazio)

print("-*-"*30)

#6-
print("Exercicio 6")
pessoa = {
    "Nome": "Bruno",
    "Idade": 18,
    "Peso": 70.5
}
print(pessoa)

print("*-*"*30)

#7-
print("Exercicio 7")
pessoa.setdefault("Profissão", "Programador")
print(pessoa)

print("-*-"*30)

#8-
print("Exercicio 8")
notas = [10, 7]
aluno = {
    "Nome": "Jorgin",
    "Notas": notas,
    "Situação": "Aprovado!"
}
print(aluno)

print("*-*"*30)

#9-
print("Exercicio 9")
tupla = (22, 2003)
dicionario = {"Valor1": 1, "Valor2": 2}
listaCompleta = [
    "String",
    tupla,
    dicionario,
    572.89
]
print(listaCompleta)

print("-*-"*30)

#10-
print("Exercicio 10")
frase = "Cientista de Dados é o profissional mais sexy do século XXI"
print(frase[1:18])
print("-*-"*10, "Finalizado exercicios capitulo 2", "-*-"*10)
