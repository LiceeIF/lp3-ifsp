'''
Ex03 - Contador de Vogais e Consoantes: 
Peça ao usuário para digitar uma frase e retorne 
o número de vogais e consoantes na frase.
'''
def vogal(char):
    vogais = "aeiouAEIOU"
    return char in vogais

def consoante(char):
    return char.isalpha() and not vogal(char)

frase = input("Digite uma frase: ")

num_vogais = 0
num_consoantes = 0

for char in frase:
    if vogal(char):
        num_vogais += 1
    elif consoante(char):
        num_consoantes += 1

print("Número de vogais:", num_vogais)
print("Número de consoantes:", num_consoantes)