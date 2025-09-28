class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        
    
    def setter_valor(self, valor: int) -> None:
        self.__valor = valor 
    
    
    @property
    def getter_valor(self):
        return self.__valor


classe_pessoal = MinhaClasse()
classe_pessoal.setter_valor(50)
print(classe_pessoal.getter_valor)

