def calcularMedia(numros,apenas_inteiros= False):
    #passo 1: calculas a soma de todos os itens da lista e dividir pelo tamanho dela
    soma = sum (numeros)
    total_itens = len(numeros)
    media = soma/total_itens

    #passo 2: verificar o parâmetro opcional
    if apenas_inteiros:
        return int(media) #caso seja verdadeiro, retornar a média como um número inteiro
    return media #caso seja falso, retornar a média como um número decimal

#exemplo de uso da função
numeros = [10, 20, 30, 40, 50]
media_decimal = calcularMedia(numeros)
media_inteira = calcularMedia(numeros, apenas_inteiros=True)