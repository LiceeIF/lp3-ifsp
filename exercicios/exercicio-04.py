'''
Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X.

Exemplos válidos:

    BR0001X
    BR1236X
    BR9999X

Exemplos inválidos:

    br0001X
    BR126X
    BR99999X
    BR9999Y
    
Crie uma função em Python que implementa essa verificação
'''

# precisa verificar se está no UPPERCASE
# precisa verificar se há 4 números após o BR
# precisa verificar se há 1 letra X ou Y como último caracter

def verificar_identificador(identificador):
    if len(identificador) == 7 and identificador[0:2] == 'BR' and identificador[2:6].isnumeric() and (identificador[6] == 'X' or identificador[6] == 'Y'):
        print('Seu identificador é válido')
    else:
        print('Seu identificador é inválido')

identificador = input('Insira seu identificador: ')
verificar_identificador(identificador)
