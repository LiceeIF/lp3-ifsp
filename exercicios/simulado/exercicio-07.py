'''
Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca.
O programa começa com uma palavra oculta 
(o usuário não vê) e o usuário tenta adivinhar a palavra, letra por 
letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
'''

import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "algoritmo", "linguagem"]
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += "_"
        return resultado

def jogar_forca():
    palavra = escolher_palavra()
    tentativas_restantes = 6
    letras_corretas = []
    letras_erradas = []
    
print("Bem-vindo ao jogo da forca!")
print("A palavra tem", len(palavra), "letras.")

while tentativas_restantes > 0:
    print("\nPalavra:", mostrar_palavra_oculta(palavra, letras_corretas))

if len(letras_erradas) > 0:
    print("Letras erradas:", " ".join(letras_erradas))

tentativa = input("Digite uma letra: ").lower()

if tentativa in palavra:
    letras_corretas.append(tentativa)
if len(set(letras_corretas)) == len(set(palavra)):
    print("\nParabéns! Você acertou a palavra:", palavra)
else:
    letras_erradas.append(tentativa)

tentativas_restantes -= 1
print("Letra incorreta. Você tem", tentativas_restantes, "tentativas restantes.")

if tentativas_restantes == 0:
    print("\nVocê perdeu! A palavra era:", palavra)

jogar_forca()