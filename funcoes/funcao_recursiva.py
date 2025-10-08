def Fatorial(N):

    if N < 1:
        print(1)
        return 1
    else:
        fat = N * Fatorial(N-1)
        print(f"O fatorial de {N} é {fat}")
        return fat

Fatorial(5)