
compras = list()
itens = dict()
valor_Parcial = 0
total = 0


def Linha():
    print("-" * 50)


Linha()
print("LISTA DE COMPRAS".center(50))
Linha()
print()
while True:
    try:
        print('\033[31mDigite sair para encerrar a lista\033[m')
        itens['produto'] = str(input("Produto: ")).lower()
        if itens['produto'] == 'sair':
            Linha()
            break
        itens['quantidade'] = int(input("Quantidade: "))
        itens['preço'] = float(input("Preço: R$ "))
        total = itens['quantidade'] * itens['preço']
        valor_Parcial += total
        compras.append(itens.copy())
        itens.clear()
        Linha()
        print(f"Valor parcial: R$ {valor_Parcial:.2f}")
        Linha()
    except ValueError:
        print("\033[31mValor inválido. Tente novamente.\033[m")
print("Lista de Compras:")
for item in compras:
    print(f"Produto: {item['produto']}| Quantidade: {item['quantidade']}| Preço: R$ {item['preço']:.2f}")
total = sum(item['quantidade'] * item['preço'] for item in compras)
Linha()
print(f"\nValor total da compra: R$\033[32m {valor_Parcial:.2f}\033[m")
Linha()

