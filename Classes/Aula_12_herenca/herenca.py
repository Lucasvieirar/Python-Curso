class Manifero:
    def __init__(self, localizacao: str) -> None:
        self.localizacao = localizacao
    def andar(self) -> None:
        print(f"O animal esta andando pelo {self.localizacao}")

class Cachorro(Manifero):
    def __init__(self, localizacao: str) -> None:
        super().__init__(localizacao)
        
    def latir(self) -> None:
        print("O cachorro esta latindo")
        self.andar()

dog = Cachorro("brasil")
dog.latir()
valor = dog.localizacao
print(valor)
