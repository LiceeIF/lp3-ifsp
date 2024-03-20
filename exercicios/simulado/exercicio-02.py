# Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

tabuada = int(input("Insira o número que você deseja ver a tabuada: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))