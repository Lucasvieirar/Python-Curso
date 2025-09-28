def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] += 2
        pos += 1


valores = [6,5,9,3,1,4,7]

dobra(valores)
print(valores)
