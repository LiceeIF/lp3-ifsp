'''
Ex08 - Função de Contagem de Palavras: Escreva uma
função que receba uma string (frase) como argumento
e retorne um dicionário onde as chaves são as palavras
únicas no texto e os valores são o número de vezes que
cada palavra aparece no texto. Depois, teste a função com
diferentes textos fornecidos pelo usuário. 
'''
def contar_palavras(frase):
    # Dividir a frase em palavras
    palavras = frase.split()

    # Inicializar o dicionário para armazenar as contagens de palavras
    contagem = []

    # Contar as palavras e armazenar as contagens no dicionário
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

# Teste da função com diferentes textos fornecidos pelo usuário
while True:
    texto = input("Digite um texto (ou 'sair' para encerrar): ")
    if texto.lower() == 'sair':
        break
    resultado = contar_palavras(texto)
    print("Contagem de palavras:", resultado)

# Entrada: joao ama maria e a maria ama o joao
# saida: Contagem de palavras: {'joao': 2, 'ama': 2, 'a': 2, 'maria': 2, 'e': 1, 'o': 1}