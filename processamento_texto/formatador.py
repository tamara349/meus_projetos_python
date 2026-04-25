def criar_formatador(etiqueta):
    def formatar(mensagem):
        return f'[{etiqueta.upper()}] {mensagem}'
    return formatar

# Exemplo de uso
aviso = criar_formatador('aviso')
erro = criar_formatador('erro')
print(aviso('O sistema reiniciará em 5 minutos.'))
print(erro('Ocorreu um erro inesperado.'))
cuidado = criar_formatador('cuidado')
print(cuidado('Tenha cuidado ao usar esta função.'))