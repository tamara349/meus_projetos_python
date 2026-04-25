def calcular_preco_final(valor_base):
    def aplicar_imposto(preco):
        return preco * 1.10
    valor_com_taxa = aplicar_imposto(valor_base)
    valor_do_imposto = valor_com_taxa - valor_base
    return valor_com_taxa, valor_do_imposto

final,taxa = calcular_preco_final(100)
print(f"Valor final: {final:.2f}, Valor do imposto: {taxa:.2f}")