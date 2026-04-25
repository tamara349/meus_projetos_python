def criar_contador():
    numero = 0
    def contar():
        nonlocal numero
        numero += 1
        return numero
    return contar

meu_contador = criar_contador()
print(meu_contador())  # Saída: 1
print(meu_contador())  # Saída: 2
