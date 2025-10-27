#injecao-> uma classe relacionada a outra
#exemplo: uma pessoa tem atributo celular 
# e tenho uma classe celular que é injetada nesse atributo

class Celular:

    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    def enviar_mensagem(self, mensagem: str) ->None:
        print(f"enviando mensagem: {mensagem}")
    
    def abrir_emails(self) -> None:
        print("Abrindo Emails..")

    def abrir_youtube(self) -> None:
        print("Abrindo Youtube...")



class Pessoa:
    def __init__(self, celular: Celular) -> None:
        self.celular = celular

    def pedir_pizza(self) -> None:
        print("Buscando o celular...")
        print("Definindo valor")
        self.celular.enviar_mensagem("quero uma pizza")
        print("Aguardando o pedido")
    def estudar(self) -> None:
        print("Sentando no computador")
        self.celular.abrir_youtube()
        print("vendo video")

android = Celular("samsung")
iphone = Celular("iphone")

p1 = Pessoa(android)
p2 = Pessoa(iphone)

p1.pedir_pizza()
print("----------")
p2.estudar()