#ler e salvar no diretorio
class CsvHandler:
    def __init__(self, directory) -> None:
        self.dir = directory

    def inser_data_in_vsc(self, data):

        print(f"inserindo {data} em {self.dir}")

    def read_data(self):
        print(f"read data in {self.dir}")

csv_handle = CsvHandler("caminho/do/diretgorio")
csv_handle.read_data()