class ConectorBancoDeDados:
    def __init__(self) -> None:
        self.connection = None

    def conectar_ao_banco(self) -> None:
        self.connection = True
class RepositorDebanco:
    def __init__(self, conexao: ConectorBancoDeDados):
       self.__conexao = conexao

    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return [1,2,3,4,5]
        return None
class RegraDeNegocio:
    def __init__(self, repo: RepositorDebanco) -> None:
        self.__repo = repo

    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()
        if not dados:
            print("Dados nao econtrados. Verifique sua conexao com a banco")
        else:
            reposta = 0
            for dado in dados:
                reposta += dado
            print(f"o resultado e: {reposta}")

conn = ConectorBancoDeDados()
conn.conectar_ao_banco()

repo = RepositorDebanco(conn)
regra  = RegraDeNegocio(repo)

regra.calcular_resultados()
