class Loja:
    taxa = 1.15

    def __init__(self, valor: float):
        self.valor_produto_bruto = valor

    def conslta_valor_do_produto(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f"valor do produto: {valor_produto:.2f}")

    @classmethod
    def editar_taxa_do_produto(cls, valor: float):
        cls.taxa = valor

loja_praia = Loja(30.50)
loja_shopping = Loja(10.39)
loja_rua = Loja(20.33)

loja_praia.conslta_valor_do_produto()
loja_shopping.conslta_valor_do_produto()
loja_praia.conslta_valor_do_produto()

loja_praia.editar_taxa_do_produto(1.35) #para todas as lojas
print("Taxa editada")

loja_praia.conslta_valor_do_produto()
loja_shopping.conslta_valor_do_produto()
loja_praia.conslta_valor_do_produto()




        