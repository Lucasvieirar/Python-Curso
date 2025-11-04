#Em python utilizamos classes abstratas para criar interface

from abc import ABC, abstractmethod

class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self)  -> None:
        pass

    @abstractmethod
    def ir_para_casa(self)  -> None:
        pass

    @abstractmethod
    def horario_da_almoco(self)  -> None:
        pass
class Professor(Trabalhador): #em python estamos implementando a interface
    def trabalhar(self)  -> None:
        print("O professor esta trabalhando")
    
    def ir_para_casa(self)  -> None:
        print("O professor esta indo para casa")

    def horario_da_almoco(self) -> None:
        print("O professor esta almoçando")

class Engenheiro(Professor):
    def trabalhar(self)  -> None:
        print("O Engenheiro esta trabalhando")
    
    def ir_para_casa(self)  -> None:
        print("O Engenheiro esta indo para casa")

    def horario_da_almoco(self) -> None:
        print("O Engenheiro esta almoçando")

def comunicar_o_trabalhador(trabalhador: Trabalhador): #Tipei para o tipo Trabalhador, para a classe Trabalhador
    trabalhador.trabalhar()
    print("Comunicar o trabalhador para ir casa")
    trabalhador.ir_para_casa()

p1 = Professor()
e1 = Engenheiro()

comunicar_o_trabalhador(p1)
print("\n")
comunicar_o_trabalhador(e1)