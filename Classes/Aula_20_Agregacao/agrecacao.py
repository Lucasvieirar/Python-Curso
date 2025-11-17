class Produtos:
    def __init__(self, nome: str, valor: int) -> None:
        self.__nome= nome
        self.__valor = valor

    def informacoes_do_produto(self) -> None:
        print(f"Produto: {self.__nome} - Valor: {self.__valor}")

class CarrinhoCompras:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produtos(self, produto: Produtos) -> None:
        self.__produtos.append(produto)
    
    def finalizar_compras(self) -> None:
        print("Compra finalizada")
        print(" Produtos:")
        for product in self.__produtos:
            product.informacoes_do_produto()
banana=Produtos("banana", 3)
pera = Produtos("pera", 2)
uva = Produtos("uva", 4)

carrinho = CarrinhoCompras()
carrinho.adicionar_produtos(banana)
carrinho.adicionar_produtos(pera)
carrinho.adicionar_produtos(uva)

carrinho.finalizar_compras()