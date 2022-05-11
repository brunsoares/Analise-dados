class Pessoa:
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def printPessoa(self):
        print(f"Pessoa: \n "
              f"Nome: {self.nome} \n"
              f"Cidade: {self.cidade} \n"
              f"Telefone: {self.telefone} \n"
              f"Email: {self.email} ")