def caixa_eletronico(): 
    # Lista de cédulas disponíveis
    cedulas = [200,100, 50, 20, 10, 5, 2,1] 
 # Solicita o valor do saque ao usuário
    try: 
        valor = int(input("Digite o valor do saque: ")) 
 # Verifica se o valor é positivo e múltiplo de 2
        if valor <= 0: 
            print("Erro: O valor deve ser positivo.")

        else: 
            print("Cédulas entregues:")
           # Calcula a quantidade de cada cédula necessária para o saque 
            for cedula in cedulas: 
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f"{quantidade} cédulas de R$ {cedula}")
                    valor = valor % cedula # Atualiza o valor restante para o próximo cálculo
 
    except ValueError: 
        print("Erro: Digite um valor numérico válido.") 
 
caixa_eletronico()