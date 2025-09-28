class MinhaClasse:

    estatico = "Padrão"  #variavel estatica, uma copia dela para toda a classe

    
    def __init__(self, estado) -> None:
        self.estado = estado
        print(self.estado)

objeto = MinhaClasse(True) #acesso plea classe
objeto2 = MinhaClasse(True)

MinhaClasse.estatico = "mudei" #mudo a variavel estatica

print(objeto.estado) #pelo atributo

print(objeto2.estatico) #acesso varivael global

print(MinhaClasse.estatico)