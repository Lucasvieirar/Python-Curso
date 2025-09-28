# SOLID

# S - Responsibilidade única - Single Responsabilty -> Modulo deve ter um, e apenas um motivo para alteração. Separar funcionalidade para partes do seu sistema

class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) ->None:
        if isinstance(nome, str) and isinstance(idade, int):  #1 validação dos dados
            print("Acessando banco de dados....")  
            print(f"Cadastrar usurio {nome}, idade{idade}")  #2 acessar dados

        else:                                               #3 tratar dados 
            print("dados invalidos")

