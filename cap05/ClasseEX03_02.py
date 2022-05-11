from cap05.ClasseEX03_01 import Smartphone
from playsound import playsound


class MP3Player(Smartphone):
    def __init__(self, tamanho, interface, capacidade):
        super().__init__(tamanho, interface)
        self.capacidade = capacidade

    def tocarMusica(self):
        print("Aproveite sua Música!")
        playsound('arquivos/enemyMusic.mp3')
