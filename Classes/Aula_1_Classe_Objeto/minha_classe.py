class MinhaClasse:
    def __init__(self, info): #construtor, primeiro a ser chamado
        self.atributo_1 = "meu atributo"  #atributos, qualquer informação
        self.atributo_2 = [1,2,3]  

        self.atributo_3 = info

    def metodo_1(self):   #metodo
        print("minha ação")
        print(self.atributo_2) #printa atributo dois
        return "ola mundo"
    
    def metodo_2(self, numero):
        print(self.atributo_2[1] + numero)
        
    def metodo_3(self):
        self.atributo_2()

minha_classe=  MinhaClasse("info")

response=minha_classe.metodo_1() #retorno rreturn
print(response)
minha_classe.metodo_2(3)