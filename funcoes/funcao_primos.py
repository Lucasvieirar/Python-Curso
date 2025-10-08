# Função que determina se um número é primo ou não


def Primo(P):
    
    if P <= 1:
        return "ERRO"
    elif P == 2:
        return 1
    elif P % 2 ==0:
        return
    else:
        raiz = P ** 0.5
        i = 3
        while i <= raiz:
            if P % i == 0:
                return 0
        return 1
    
print(Primo(5))