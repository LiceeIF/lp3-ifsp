'''
Ex05 - Verificador de Palíndromos: Solicite ao usuário que 
digite uma palavra ou frase e verifique se é um palíndromo
(ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).
'''

def palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

entrada = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if palindromo(entrada):
    print("A palavra digitada é um palíndromo.")
else:
    print("A palavra digitada não é um palíndromo.")