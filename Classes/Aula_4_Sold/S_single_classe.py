class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validade_input(nome, idade):
            self.__registrar_usuario(nome, idade)
        else:                                              
            self.__error_handle()


    def __validade_input(self, nome: str, idade: int):
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __registrar_usuario(self, nome: str, idade: int) -> None:
        print("Acessando banco de dados....")  
        print(f"Cadastrar usurio {nome}, idade{idade}")

    def __error_handle(self) -> None:
        print("dados invalidos")