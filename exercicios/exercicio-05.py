# Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.
def verificar_identificador(identificador):
    if len(identificador) == 7 and identificador[0:2] == 'BR' and identificador[2:6].isnumeric() and (identificador[6] == 'X' or identificador[6] == 'Y'):
        print('Seu identificador é válido')
    else:
        print('Seu identificador é inválido')

print('BEM-VINDO AO PROGRAMA')
identificador = input('Insira seu identificador: ')
verificar_identificador(identificador)
