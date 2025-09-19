class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf

    def apresentar(self):
        print(f"minha altura é {self.altura}")
        self.__coletar_documento()

    def __coletar_documento(self): # __ significa 'esconder', acessados só dentro da classe
        print(f"meu documento {self.__cpf}")
    
minha_pessoa = Pessoa("1,80", "1851548")
minha_pessoa.__cpf = "123abc"

print(minha_pessoa.__cpf)
minha_pessoa.__coletar_documento()