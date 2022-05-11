#Manipulação de arquivos - leitura
arquivoLeitura =  open("arquivos/arquivo.txt", "r") #r - read
print("Conteudo: \n", arquivoLeitura.read())
print("Quantidade de caracteres: \n", arquivoLeitura.tell())
print("Apenas os 5 primeiros caracteres: \n", arquivoLeitura.read(10))
#For para ler os arquivos
for linhas in open("arquivos/arquivo.txt", "r"):
    print(linhas)
arquivoLeitura.close()

#Manupulação de arquivos - gravação
arquivoGravacao = open("arquivos/arquivo.txt", "w") #w - write
arquivoGravacao.write("gravacao pelo codigo ;-;")
arquivoGravacao.close()

#Manipulação de arquivos - adicionar
arquivoAdicionar = open("arquivos/arquivo.txt", "a") #a - append
arquivoAdicionar.write("\nAdicionando informacoes pelo codigo")
arquivoAdicionar.close()

#Manipulando arquivos csv
arquivoCSV = open("arquivos/salarios.csv", "r")
dados = arquivoCSV.read()
linhas = dados.split("\n")
print(linhas)


