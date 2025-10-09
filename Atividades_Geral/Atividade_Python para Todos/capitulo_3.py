# Exercício 1: Reescreva seu programa de pagamento, para pagar ao fun
# cionário 1.5 vezes o valor da taxa horária de pagamento pelo tempo
# #  trabalhado acima de 40 hora

# horas = float(input("Digite o número de horas trabalhadas: "))

# taxa = float(input("Digite o valor da taxa por hora (R$): "))
# if horas <= 40:
#     valor_pago = horas * taxa
#     print(valor_pago) 

# else:
#     valor_pago = 40 * taxa
#     hora_extra = horas - 40
#     valor_extra = hora_extra * taxa * 1.5
#     valor_pago_extra = valor_extra + valor_pago
#     print(valor_pago_extra)


#  Exercício 2: Reescreva seu programa de pagamento utilizando try e
#  except, de forma que o programa consiga lidar com entradas não numéri
# cas graciosamente, mostrando uma mensagem e saindo do programa. A
#  seguir é mostrado duas execuções do programa

try :
    horas = float(input("Digite o número de horas trabalhadas: "))

    taxa = float(input("Digite o valor da taxa por hora (R$): "))


    

    if horas <= 40:
        valor_pago = horas * taxa
        print(valor_pago) 

    else:
        valor_pago = 40 * taxa
        hora_extra = horas - 40
        valor_extra = hora_extra * taxa * 1.5
        valor_pago_extra = valor_extra + valor_pago
        print(valor_pago_extra)

except ValueError:
    
    print(" Erro, por favor utilize uma entrada numérica")
