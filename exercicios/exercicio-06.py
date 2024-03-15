'''
Ex06. Crie um programa em Python que recebe como entrada o comprimento, 
altura e a largura de um aquário e calcule as seguintes informações.

    O volume do aquário em litros;
    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

    Volume é dado por (comprimento * altura * largura) / 1000
    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

Utilize funções.
'''

def calcular_volume(comprimento, altura, largura):
    volume = (comprimento * altura * largura)/100
    return volume

def calcular_potencia(volume, temperatura_desejada, temperatura_ambiente):
    potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    return potencia

def calcular_filtragem(volume):
    filtragem_hora = volume * 2 #colocar 2 pois é o mínimo
    return filtragem_hora

comprimento = float(input("Digite o comprimento do aquário em centímetros: "))
altura = float(input("Digite a altura do aquário em centímetros: "))
largura = float(input("Digite a largura do aquário em centímetros: "))
temperatura_desejada = float(input("Digite a temperatura desejada dentro do aquário em graus Celsius: "))
temperatura_ambiente = float(input("Digite a temperatura ambiente em graus Celsius: "))

volume = calcular_volume(comprimento, altura, largura)
potencia_termostato = calcular_potencia(volume, temperatura_desejada, temperatura_ambiente)
filtragem_por_hora = calcular_filtragem(volume)

print("\nInformações do Aquário:")
print("Volume do aquário:", volume, "litros")
print("Potência do termostato necessária:", potencia_termostato, "watts")
print("Quantidade de filtragem por hora necessária:", filtragem_por_hora, "litros por hora")
