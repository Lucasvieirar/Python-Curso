#Objetos podem ser subistituitos por seus subtipo
#sem que isso afete a execução correta do porgrama

class Animal:
    def alimentar(self):
        print("O animal está se alimentando")

class Cachorro(Animal):
    def latir(self):
        print("O cachorro está latindo")

class Peixe(Cachorro): # quebra do principio Liskov
    def nadar(self):
        print("O peixe estada nadando")
    def latir(self):
        raise Exception("Peixe não late")
    
def verificar_animal(animal: any):
    animal.latir()

animal = Animal()
animal2 = Cachorro()
animal3 = Peixe()
verificar_animal(animal3)