# class Cubo:
#     pass        #classe vazia

# print(type(Cubo))

class Cubo:
    '''calcular area do cubo ''' #cria Docstring
    
    def __init__(self, valor): #metodo cosntrututor da classe
        self.valor = valor

    def calcula_cubo(self) -> str:
        cubo = self.valor * self.valor * self.valor
        return "Cubo calculo:" + str(cubo)

calculo = Cubo(8)

area_do_cubo = calculo.calcula_cubo()

print(area_do_cubo)

    
        
