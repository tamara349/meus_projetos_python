def criar_gerador_seguro(prefixo_secreto):
    def gerar(senha_usuario):
        return prefixo_secreto + senha_usuario
    return gerar

gerador_admin = criar_gerador_seguro("ADM99")
print(gerador_admin("145"))