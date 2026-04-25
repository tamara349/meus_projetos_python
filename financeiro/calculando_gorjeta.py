def calcular_gorjeta(valor, percentual):
    gorjeta = valor * (percentual/ 100)
    return gorjeta


valor_da_conta = float(input("Digite o valor da conta: "))
percentual_da_gorjeta = float(input("Digite o percentual da gorjeta (ex: 15 para 15%): "))
gorjeta = calcular_gorjeta(valor_da_conta, percentual_da_gorjeta)
print(f"A gorjeta a ser dada é: R$ {gorjeta:.2f}")
print(f"O valor total a ser pago é: R$ {valor_da_conta + gorjeta:.2f}")