#  Exercício 2: Escreva um programa que use inputs para solicitar ao
#  usuário seu nome e, em seguida, faça um cumprimento.

nome = input("Digite seu nome: ")
print(nome)
tam = len(nome)
print(f"O tamanho de{nome} é {tam}")

# Exercício 3: Escreva um programa que solicite ao usuário as horas e o
#  valor da taxa por horas para calcular o valor a ser pago por horas de
#  serviço.
horas = float(input("Digite o número de horas trabalhadas: "))

taxa = float(input("Digite o valor da taxa por hora (R$): "))

valor_pago = horas * taxa

print(f"O valor a ser pago pelas {horas} horas é {valor_pago:.2f}")

# Exercício 4: Suponha que executamos as seguintes declaração por
#  atribuição: Largura = 17
            #    Altura = 12.0

# Para cada uma das expressões a seguir, escreva o valor da expressão e o tipo (do
#  valor da expressão).
#  1. Largura//2
#  2. Largura/2.0
#  3. Altura/3
#  4. 1 + 2 * 5 
Largura = 17
Altura = 12.0

x1 = Largura//2           
x2 = Largura/2.0
x3 = Altura/3
x4 = 1 + 2 * 5 
print(x1,x2,x3,x4)

# Exercício 5: Escreva um programa que solicite ao usuário uma tem
# peratura Celsius, converta para Fahrenheit, e mostre a temperatura
#  convertida.
C = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (C *9/5) + 32

print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F ")