#definimos a função para formatar os produtos
def formatar_produtos(lista_suja):
    #criamos uma lista vazia para armazenar os produtos formatados
    lista_formatada = []
    numero = 1 # variável para numerar os produtos
    #percorremos a lista suja de produtos
    for item in lista_suja:
       #arrumamos o item: colocamos o numero e deixamos a primeira letra maiúscula
       item_arrumado = f"{numero} - {item.capitalize()}"

         #adicionamos o item arrumado na lista formatada
    
       lista_formatada.append(item_arrumado)
            #incrementamos o número para o próximo produto
       numero += 1
    #retornamos a lista formatada
    return lista_formatada

#exemplo de uso da função
produtos_sujos = ["arroz", "feijão", "macarrão", "óleo"]
produtos_formatados = formatar_produtos(produtos_sujos)
print(produtos_formatados)