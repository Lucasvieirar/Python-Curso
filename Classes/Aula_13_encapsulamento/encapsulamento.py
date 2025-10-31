class Mamifero:
    def __init__(self, localizacao) -> None:
        self.localizao = localizacao
        self._tamanho = 1.23
    def andar(self) -> None:
        print(f"O animal esta andando pelo {self.localizao}")

    def _dormir(self) -> None:      #protegido
        print("O Animal está dormindo")

class Gato(Mamifero):
    def __init__(self, localizacao):
        super().__init__(localizacao)
    def miar(self) -> None:
        print("O gato esta miando")
        self._dormir()
        print(self._tamanho)

cat = Gato("Argentina")

cat.miar()
cat._dormir()  #elementos protegidos são acessados dentro da classe, sem seres objetos
print(cat._tamanho)