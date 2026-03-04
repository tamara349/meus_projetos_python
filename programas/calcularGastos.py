def calcularGastos(gastos):
    total_gastos = sum(gastos)
    for gasto in gastos:
        if gasto > 200:
            print(f"Gasto de {gasto} é alto.")
        elif gasto > 100:
            print(f"Gasto de {gasto} é moderado.")
        else:
            print(f"Gasto de {gasto} é baixo.")
    return total_gastos

# Exemplo de uso
gastos = [int(x) for x in input("Digite os gastos separados por vírgula: ").split(",")]
total = calcularGastos(gastos)
print(f"Total de gastos: {total}")