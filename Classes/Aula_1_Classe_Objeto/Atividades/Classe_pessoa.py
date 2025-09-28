#Crie uma classe pessoa com: nome, idade e altura
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def seu_nome(self):
        print(f"olá meu nome é {self.nome}")
        
       

    def sua_altura(self):
        print(f"tenho {self.altura}")

    def sua_idade(self):
        print(f"minha altura {self.idade}")

minha_pessoa = Pessoa("lucas", "18", "1.80")

minha_pessoa.seu_nome()
minha_pessoa.sua_altura()
minha_pessoa.sua_idade()






        