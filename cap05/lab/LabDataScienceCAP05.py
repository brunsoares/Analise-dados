import AuxiliarClass as aux

palavraEscolhida = aux.escolherPalavra()
palavraEscondida = aux.montarPalavra(palavraEscolhida)
tentativa = 20
contador = 0
objetoAuxiliar = aux.Auxiliar(palavraEscolhida)
while True:
    if tentativa == 0:
        print("Acabou suas tentativas!")
        print(f"A palavra escolhida foi: \033[31m{palavraEscolhida}")
        break
    elif aux.tratarPalavra(palavraEscondida).replace(" ", "") == palavraEscolhida:
        fraseWin = "| \033[39mParabéns, você acertou a palavra \033[32m"+palavraEscolhida+"\033[39m!! \033[35m"
        print("\033[35m-*"*int((len(fraseWin)/2)-9))
        print(f"{fraseWin}", end="|\n")
        print("-*"*int((len(fraseWin)/2)-9))
        break
    print("-*-"*10, "Jogo da Forca", "-*-"*10)
    aux.printDesenho(contador)
    print(f"Palavra:    {aux.tratarPalavra(palavraEscondida)}")
    print(f"Letras inválidas: {objetoAuxiliar.listaErro}\n")
    print(f"Letras válidas: {objetoAuxiliar.listaAcerto}\n")
    print(f"Você tem {tentativa} chances ainda, boa sorte\n")
    letraTentativa = str(input("Qual letra você quer tentar?  ")).strip().lower()
    tentativa -= 1
    palavraEscondida = aux.adicionarLetra(palavraEscolhida, letraTentativa, palavraEscondida)
    objetoAuxiliar.checarLetra(letraTentativa)
    checarTentativa = objetoAuxiliar.checkStatus(letraTentativa)
    if not checarTentativa:
        contador += 1


