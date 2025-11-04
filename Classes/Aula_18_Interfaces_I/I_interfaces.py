from abc import ABC, abstractmethod

class Trabalhador(ABC): # não posso depender de uma interface que não utilizo

    @abstractmethod
    def trabalhar(self)  -> None:
        pass

    @abstractmethod
    def ir_para_casa(self)  -> None:
        pass

    @abstractmethod
    def consultar_beneficio(self)  -> None:
        pass

class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print("O Professor esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O Professor esta indo para casa")

    def consultar_beneficios(self) -> None:
        print("Consultando beneficios da CLT")

class ProfessorSubstituto(Trabalhador):
    def trabalhar(self) -> None:
        print("O Professor Substituto esta trabalhando")

    def ir_para_casa(self) -> None:
        print("O Professor Substituto esta indo para casa")

    def consultar_beneficios(self) -> None:  # Quebra da segregação
        raise Exception("O Professor Substituto nao tem beneficios")
    
p1 = ProfessorSubstituto()
p1.consultar_beneficio() # Quebra da segregação
 