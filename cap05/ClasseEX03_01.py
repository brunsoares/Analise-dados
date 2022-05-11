class Smartphone:
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

    def printModelo(self):
        print(f"Smartphone: \n"
              f"Tamanho -> {self.tamanho} \n"
              f"Interface -> {self.interface}")