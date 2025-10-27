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

android = Celular("samsung")
iphone = Celular("iphone")

class Pessoa:
    def __init__(self, celular: Celular) -> None:
        self.celular = celular

pessoa = Pessoa(iphone)


