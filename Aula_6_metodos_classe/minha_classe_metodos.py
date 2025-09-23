class MinhaClasse:

    estatico = "Padrão"  #não é acessivel internamente, apenas com self 
    
    def __init__(self, estado) -> None:
        self.estado = estado
        print(self.estado)

    def variavel_classe(self):  #não é acessivel internamente 
        print(self.estatico) #agora com self eu consigo

    @classmethod  #consigo ter acesso e modificação para toda classe
    def alterar_variavel(cls):
        cls.estatico = "mudei"

objeto = MinhaClasse(True) 
objeto2 = MinhaClasse(True)

objeto.variavel_classe()

objeto.alterar_variavel() #altera so para o objeto 1

print(objeto.estatico) 

print(objeto2.estatico)
print(MinhaClasse.estatico)
