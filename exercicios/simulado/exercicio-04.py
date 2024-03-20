'''
Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. 
O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de 
votos de cada candidato e quem foi o vencedor. 
'''
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

num_votos_total = 0

while True:
    print("Candidatos:")
    print("1. Candidato A")
    print("2. Candidato B")
    print("3. Candidato C")
    print("0. Encerrar votação")

    voto = int(input("Digite o número do candidato em que deseja votar (ou 0 para encerrar): "))

    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 3 para votar.")
    num_votos_total += 1

    print("\nResultados da votação:")
    print("Candidato A: ", votos_candidato1, " votos")
    print("Candidato B: ", votos_candidato2, " votos")
    print("Candidato C: ", votos_candidato3, " votos")
    if votos_candidato1 > votos_candidato2 and votos_candidato1 > votos_candidato3:
        print("\nCandidato A venceu!")
    elif votos_candidato2 > votos_candidato1 and votos_candidato2 > votos_candidato3:
        print("\nCandidato B venceu!")
    elif votos_candidato3 > votos_candidato1 and votos_candidato3 > votos_candidato2:
        print("\nCandidato C venceu!")
    else:
        print("\nHouve um empate!")
    break

# nao sei como fazer o usuario votar varias vezes