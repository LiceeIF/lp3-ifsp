'''
Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

    Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
    Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
    Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
    Compras iguais ou superiores a R$ 500,00 - 15% de desconto
'''

valor = float(input('insira o valor da sua compra'))

if valor < 9.99:
    print(f'esse valor não se aplica desconto')
elif valor >= 10.00 and valor <= 99.99:
    valor_com_desconto5 = valor - (valor * 0.05)
    print(f'O valor atual será de', valor_com_desconto5)
elif valor >= 100.00 and valor <= 499.99:
    valor_com_desconto10 = valor - (valor * 0.10)
    print(f'O valor atual será de', valor_com_desconto10)
else:
    valor_com_desconto15 = valor - (valor * 0.15)
    print(f'O valor atual será de', valor_com_desconto15)

