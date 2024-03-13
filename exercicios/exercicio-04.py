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

identificador = input('insira seu identificador')

while len(identificador) == 7 and identificador[0] == 'B' and identificador[1] == 'R':
    if identificador[2].isnumeric and identificador[3].isnumeric and identificador[4].isnumeric and identificador[5].isnumeric:
        print('seu identificador é válido')
    else:
        print('seu identificador é inválido')
break
