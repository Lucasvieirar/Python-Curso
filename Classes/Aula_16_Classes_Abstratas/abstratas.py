from abc import ABC, abstractmethod
class Pessoa(ABC):  #Classe abstrata não possui objetos, só pode ser mãe
    #não crio objetos, só participo se for herança
    def correr(self):
        print("A pessoa esta correndo de manha")

    @abstractmethod #Classe filha deve criar um metodo 
    def trabalhar(self): # forço as filas a terem esse metodo
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print("O professor esta trabalhando")

p1= Professor()

p1.trabalhar()
p1.correr()