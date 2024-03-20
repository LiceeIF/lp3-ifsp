# Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um 
# número entre 1 e 100 que o programa escolheu aleatoriamente. Informe 
# ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

import random

numero = random.randint(1, 100)

print(numero)

while True:
    chute = int(input('Insira um número:'))
    if chute == numero:
        print('parabéns! você acertou')
        break
    if chute > numero:
        print('tente novamente, seu número está longe')
    else:
        print('tente outro número, este está muito baixo')