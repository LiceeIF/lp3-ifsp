'''
Ex06 - Conversor de Notas Escolares: Baseado em uma
pontuação fornecida pelo usuário (0 a 100), converta 
para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
'''
nota = float(input('Insira sua nota de 0 a 100'))

def converter_notas(nota):
    if nota >= 89:
        return 'A'
    elif nota >= 80:
        return 'B'
    elif nota >= 70:
        return 'C'
    elif nota >= 60:
        return 'D'
    else:
        return 'F'
    
if 0 <= nota <= 100:
    nota = converter_notas(nota)
    print('A nota será:', nota)
else:
    print('A nota informada foi inváida, por favor, insira uma válida!')