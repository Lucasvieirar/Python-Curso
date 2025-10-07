class Interruptor:
    def __init__(self, comodo: str):
        self.comodo = comodo

    def acender(self):
        print(f"Estou acendendo a luz do comodo: {self.comodo}")

    def apagar(self):
        print(f"Estou Apagando a luz do comodo: {self.comodo}")

class Pessoa:
    def acender_luzes(self, interruptor: Interruptor): # interruptor: Interruptor é a
        interruptor.acender()                                                    # sintaxe que faz a associção com a classe Interruptor


    def apagar_luzes(self,  interruptor: Interruptor):
        interruptor.apagar()

    def dormir(self):
        print("A pessoa foi dormir")

lucas = Pessoa()
Interruptor_sala = Interruptor("sala")
Interruptor_quarto = Interruptor("quarto")

lucas.acender_luzes(Interruptor_sala)
lucas.acender_luzes(Interruptor_quarto)

