#Desenvolver a cálculadora
def mensagens():
    mensagem = "Selecione a opção desejada: \n"\
                "\n[1] Somar\n"\
                "[2] Subtração\n"\
                "[3] Multiplicação\n"\
                "[4] Divisão\n"\
                "[5] Sair\n"
    return mensagem

while True:
    print(mensagens())
    escolha = int(input("Digite sua opção: "))
    if escolha not in range(1,6):
        print("Opção inválida! escolha novamente")
        continue

    if escolha == 5:
        print("Adeus!")
        break

    #valores
    numero1 = int(input("Digite o primeiro valor da conta: "))
    numero2 = int(input("Digite o segundo valor da conta: "))

    #Calculos
    if escolha == 1:    #somar
        resultado = lambda num1, num2: num1+num2
        print(f"{numero1} + {numero2} = ", resultado(numero1, numero2))
        continue
    elif escolha == 2:
        resultado = lambda num1, num2: num1-num2
        print(f"{numero1} - {numero2} = ", resultado(numero1, numero2))
        continue
    elif escolha == 3:
        resultado = lambda num1, num2: num1*num2
        print(f"{numero1} x {numero2} = ", resultado(numero1, numero2))
        continue
    elif escolha == 4:
        resultado = lambda num1, num2: num1/num2
        print(f"{numero1} / {numero2} = ", resultado(numero1, numero2))
        continue
