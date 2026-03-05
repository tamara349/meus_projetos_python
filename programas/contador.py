def criar_contador(inicio=0):
    valor = inicio
    def incrementar():
        nonlocal valor # Permite modificar a variável 'valor' definida no escopo externo
        valor += 1
        return valor
    return incrementar

# Exemplo de uso
meu_contador = criar_contador(10)
print(meu_contador())  # Saída: 11
print(meu_contador())  # Saída: 12