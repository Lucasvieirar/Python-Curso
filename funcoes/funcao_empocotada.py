def contador(* num):
    for valor in num:
        print(f'{valor}', end='')
    tam = len(num)
    print(f'o tamanho de {num} é {tam}')

contador( 2 , 1, 7)
contador(8 ,8)
contador(4, 2, 9, 7)