def somar( * valores):
    s = 0
    for valor in valores:
        s += valor
    print(f'Somando os valores {valores} temos {s}')

somar(5, 2)
somar(2, 9, 1)
somar(8, 5, 10, 2)