'''
Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca.
O programa começa com uma palavra oculta 
(o usuário não vê) e o usuário tenta adivinhar a palavra, letra por 
letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.
'''

def mostrar_palavra_oculta(palavra, letras_corretas):
    resultado = ''
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado.strip()

def jogo_da_forca(palavra, tentativas):
    letras_corretas = set()
    letras_incorretas = set()
    
    print("Bem-vindo ao jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")
    
    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra_oculta(palavra, letras_corretas))
        print("Tentativas restantes:", tentativas)
        
        palpite = input("Digite uma letra: ").lower()
        
        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue
        
        if palpite in letras_corretas or palpite in letras_incorretas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if palpite in palavra:
            letras_corretas.add(palpite)
            if len(letras_corretas) == len(set(palavra)):
                print("\nParabéns! Você adivinhou a palavra:", palavra)
                return
        else:
            letras_incorretas.add(palpite)
            tentativas -= 1
            print("Letra incorreta. Tente novamente.")
    
    print("\nVocê perdeu! A palavra era:", palavra)

palavra_oculta = "paralelepipedo"
tentativas = 4
jogo_da_forca(palavra_oculta, tentativas)
