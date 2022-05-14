# Loop para pegar os valores
print("Digite 5 valores a seguir: \n")
listaVal = []
for i in range(0, 5):
    listaVal.append(int(input(f"{i+1}º -> ").strip()))

print(f"Lista atual (sem ordenação): {listaVal}")

# Loop para ordenar manualmente
for ln in range(len(listaVal)): # Rodar por toda a lista
    minimo = ln
    for ot in range(ln+1, len(listaVal)):   # Checando se tem outro valor menor que 'minimo' na lista
        if listaVal[minimo] > listaVal[ot]: # minimo é maior, substituir
            minimo = ot

    # Fazendo a troca de posição - minimo primeiro
    listaVal[ln], listaVal[minimo] = listaVal[minimo], listaVal[ln]

print(f"Lista atual (com ordenação): {listaVal}")
