#1-
print("Exercicio 1")
import ClasseEX01 as ex01
foguete = ex01.Rocket(10, 50)
foguete.print_rocket()
foguete.move_rocket(30, 20)
foguete.print_rocket()
print("-*-"*30)

#2-
print("Exercicio 2")
import ClasseEX02 as ex02
pessoa = ex02.Pessoa("Bruno", "Jundiaí", "93872600", "brunohenrique.soares@outlook.com")
print(pessoa.__getattribute__("nome"))
pessoa.__setattr__("telefone", "123456789")
print(pessoa.__getattribute__("telefone"))
print("*-*"*30)

#3-
print("Exercicio 3")
import ClasseEX03_02 as ex03
aparelho = ex03.MP3Player(30, "Interface", 200)
aparelho.printModelo()
aparelho.tocarMusica()
print("-*-"*10, "Finalizado exercicios capitulo 5", "-*-"*10)
