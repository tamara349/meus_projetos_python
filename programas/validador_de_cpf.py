def validar_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."
while True:
    cpf = input("Digite seu CPF: ")
    resultado = validar_cpf(cpf)
    if resultado == "CPF válido.":
        print(resultado)
        break
    else:
        print(resultado)
    