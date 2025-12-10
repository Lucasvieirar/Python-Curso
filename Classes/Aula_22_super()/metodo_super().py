class Pessoa:
    def __init__(self,nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.token_pessoa = self.nome + self.cpf + 'secret_key'

    def exibir_extrato(self):
        print("Exibindo o extrato")

class Cliente(Pessoa):
    def __init__(self, nome, cpf, total_compras):
        
        super().__init__(nome, cpf) #  -> herda metodo da classe pai
        self.total_compras = total_compras
        self.token_cliente = self.token_pessoa +  self.total_compras

x = Cliente("lucas", "123456789", 3)

print(x.nome)