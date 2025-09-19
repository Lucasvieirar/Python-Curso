class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        
    
    def setter(self, valor: int) -> None:
        self.__valor = valor 

    def getter(self) -> int:
        return self.__valor

classe_pessoal = MinhaClasse()

classe_pessoal.setter(10)  #alterar
valor = classe_pessoal.getter() #pegar
print(valor)