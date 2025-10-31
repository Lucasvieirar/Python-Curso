class Poli:
    def fazer(self) -> None:
        print("Estou fazendo algo")

class OutraCoisa(Poli):
    def preparar(self) -> None:
        print("Estou preparando algo")

    def fazer(self) -> None:  #sobre escreveu ao metodo de cima
        print("Estou fazendo outra coisa")

obj1 = Poli()

obj2 = OutraCoisa()

obj1.fazer()
obj2.fazer()