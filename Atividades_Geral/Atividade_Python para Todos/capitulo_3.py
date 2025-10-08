# Exercício 1: Reescreva seu programa de pagamento, para pagar ao fun
# cionário 1.5 vezes o valor da taxa horária de pagamento pelo tempo
# #  trabalhado acima de 40 hora

horas = float(input("Digite o número de horas trabalhadas: "))

taxa = float(input("Digite o valor da taxa por hora (R$): "))
if horas <= 40:
    valor_pago = horas * taxa  

else:
    
    horas_extras = horas - 40
    valor_pago = (horas_extras * taxa) + (horas_extras * taxa * 1.5)
print(f"O valor a ser pago pelas {horas} horas é {valor_pago:.2f}")
