#PRINCIPIO OPEN
#entidades de software, dever ser abertar para extensão
#mas fechadas para modificação

class Circo:
    def apresentar(self, comando: int):
        if comando == 1:
            self.__show_palhaco()

        if comando == 2:
            self.__show_malabarista()

    def __show_palhaco(self):
        print("O palhaço esta apresentando seu show")

    def __show_malabarista(self):
        print("O malabarista esta apresentando seu show")

circo = Circo()   

comando = 2
circo.apresentar(comando)