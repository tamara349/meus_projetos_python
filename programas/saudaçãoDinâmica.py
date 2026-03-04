def saudar(nome,periodo):
    #convertemos para minúsculo para facilitar a comparação
    periodo = periodo.lower()

    if periodo == "manhã":
        saudação = "Bom dia"
    elif periodo == "tarde":
        saudação = "Boa tarde"  
    elif periodo == "noite":        
        saudação = "Boa noite"
    else:
        saudação = "Olá"
    return f"{saudação}, {nome}!"
# Exemplo de uso
nome_usuario = input("Digite seu nome: ")
periodo_usuario = input("Digite o período do dia (manhã, tarde, noite): ")
mensagem = saudar(nome_usuario, periodo_usuario)
print(mensagem)
