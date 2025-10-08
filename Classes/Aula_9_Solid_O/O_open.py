#PRINCIPIO OPEN
#entidades de software, dever ser abertar para extensão
#mas fechadas para modificação

# class Circo:
#     def apresentar(self, comando: int):
#         if comando == 1:
#             self.__show_palhaco()
#                           #preciso escalonar vou aumentar exponencionalmente o tamanho do codigo
#         if comando == 2:
#             self.__show_malabarista()

#     def __show_palhaco(self):
#         print("O palhaço esta apresentando seu show")

#     def __show_malabarista(self):
#         print("O malabarista esta apresentando seu show")

# circo = Circo()   

# comando = 2
# circo.apresentar(comando)

class Artista:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def apresentar_show(self):
        print(f"O {self.tipo} esta apresentando seu show")

class Circo:
    def apresentar(self, artista: Artista):
        print("O circo esta abrindo!")
        artista.apresentar_show()
        print("O publico aplaude!")
        
circo = Circo()

palhaco = Artista("Palhaço")
magico = Artista("Magico")
malabarista =Artista("malabarista")

circo.apresentar(malabarista)