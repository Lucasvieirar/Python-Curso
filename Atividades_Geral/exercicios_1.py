
# 1
# Faça X = 0.0 e Y = 18. Verifique o tipo de dado que o Python atribuiu
#  a cada um. Faça Z = X + Y e verifique o resultado calculado e
#  armazenado em Z. Verifique com qual tipo de dado foi criado o objeto
#  Z.

x = 0.0
y = 18

print(type(x))
print(type(y))

z = x + y

print(z)

print(type(z))
# 2
#  Atribua um valor qualquer a um objeto a (minúsculo). Utilize o
#  comando type ou o comando print com o objeto A (maiúsculo). Relate
#  o que aconteceu.

a = 10

# print(A)

#erro, A não foi definido

# 3
# No IDLE, faça A = “Questão 3”, B = 25 e C = 3.9. Utilize o comando
#  type para verificar qual é o tipo de dado dos objetos A, B e C.

A =  "Questão 3"
B = 25
C = 3.9
print(type(A))
print(type(B))
print(type(C))

# 4
# Escreva a sequência de comandos necessária para o cálculo da área de
#  um triângulo de base 9 e altura 6.

base = 9
altura= 6
Area = (base * altura) / 2
print(Area)

# 5
#  Refaça o exercício 4 alterando-o de modo que a base e a altura do
#  triângulo sejam lidas do teclado. Considere-as números reais.

base = float(input("Digite a base do seu triangulo: "))
altura= float(input("Digite a altura do seu triangulo: "))

Area = (base * altura) / 2
print(f"O triangulo de base: {base} e altura {altura} é {Area}")