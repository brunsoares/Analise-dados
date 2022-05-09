# 1-
print("Exercicio 1")
diaSemana = str(input("Qual o dia de hoje? ")).lower()
if diaSemana in "sabado""domingo":
    print("Hoje é dia de descanso!")
else:
    print("Você precisa trabalhar!")

print("-*-" * 30)

# 2-
print("Exercicio 2")
frutas = ['Banana', 'Maracujá', 'Melancia', 'Morango', 'Maçã']
if frutas.count('Morango') > 0:
    print(f'Na lista de frutas, existe morango, na posição {frutas.index("Morango") + 1}')
else:
    print("Na lista não existe morangos")

print("*-*" * 30)

# 3-
print("Exercicio 3")
numeros = (1, 3, 5, 7)
numerosFinais = []
for i in range(len(numeros)):
    print(f"Número da vez: {numeros[i]}")
    valorDuplo = numeros[i] * 2
    numerosFinais.append(valorDuplo)
print(f"O valor da lista apos ser multiplicado por 2 é\n {numerosFinais}")
print("-*-" * 30)

# 4-
print("Exercicio 4")
pares = []
for i in range(100, 151):
    if i % 2 == 0:
        pares.append(i)
print(pares)
print("*-*" * 30)

# 5-
print("Exercicio 5")
while True:
    temperatura = int(input("Digite uma temperatura: "))
    if temperatura > 35:
        print(f"Ta quente, temperatura {temperatura}")
    if temperatura <= 35:
        print(f"Esfriou, tchau")
        break
print("-*-" * 30)

# 6-
print("Exercicio 6")
contador = 0
for contador in range(0, 101):
    print(contador, end=";")
    if contador == 23:
        print(f"\nEncontrou o {contador}, loop finalizado!")
        break
print("*-*" * 30)

# 7-
print("Exercicio 7")
valor = 4
listaPares = []
while valor <= 20:
    if valor % 2 == 0:
        print(f"Valor {valor} é par, adicionado!")
        listaPares.append(valor)
    valor += 1
print(f"Lista final \n {listaPares}")
print("-*-" * 30)

# 8-
print("Exercicio 8")
valores = []
for i in range(5, 45, 2):
    valores.append(i)
print(f"Valores adicionados a lista no range de 5 a 45 indo de 2 em 2 \n {valores}")
print("*-*" * 30)

# 9-
print("Exercicio 9")
temp = float(input("Qual a temperatura? "))
if temp > 30:
    print("Vista roupas leves.")
else:
    print("Busque seus casacos.")
print("-*-" * 30)

# 10-
print("Exercicio 10")
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante " \
        "como os sonhos, tem pelo menos a vantagem de existir."
countFrase = frase.count("r")
print(f"A frase contém {countFrase} R")
print("-*-"*10, "Finalizado exercicios capitulo 3", "-*-"*10)
