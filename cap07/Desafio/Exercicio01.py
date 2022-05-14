import re       # Validar a string

frase = str(input("Digite uma frase: ")).strip()
modelo = "[A-Za-z0-9 -]*$"   # Expressão regular, onde checa apenas valores normais
especial = bool(re.match(modelo, frase))
if not especial:
    print("A sua frase contém caracter especial!")
else:
    print("A sua frase não contém caracter especial!")
