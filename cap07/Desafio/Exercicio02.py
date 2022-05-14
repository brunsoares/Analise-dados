listaPrimos = []
while True:
    numero = int(input("Digite um valor [0 para sair]: ").strip())

    if numero == 0:
        break

    # Loop para checar o intervalo do valor (2 até numero) e checar divisão
    multiplos = 0
    for i in range(2, numero):
        if numero % i == 0: # O número é primo pois é multiplo de i
            print(f"Número {numero} é múltiplo de {i}")
            multiplos += 1  # Recebe um multiplo

    if multiplos == 0:
        print(f"O número {numero} é primo")
        listaPrimos.append(numero)
    else:
        print(f"O número não é primo pois tem {multiplos} múltiplos")

print(f"Os números primos digitados foram: \n {sorted(listaPrimos)}")
