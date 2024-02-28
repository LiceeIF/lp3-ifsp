# 1. NUMEROS


#1. int
idade = 20

#2. float
altura = 1.70

#3. Complex
# calculos com números complexos
numero_complexo = 1 + 2j

# 2. BOOLEANO
verdadeiro = True
falso = False


#  3. SEQUÊNCIAS
# str, list, tuple, set, dict:

# 1. str: conjunto de caracteres, ou aspas simples ou aspas duplas o código inteiro
nome = 'joao da silva'
nome = 'Maria dos Santos'

# str de múltiplas linhas
frase = """
ola amigo
parabéns, amigo
"""

# interpolação de str
nome = 'Maria'
idade = 78
mensagem = f'{nome} é uma pessoa legal! Ela tem (idade) anos.'

#Char nao existe então: usar str de tamanho 1

#como acessar um caracter em determinada string?
nome = 'Silvio Santos'
print(nome[2])

#métodos de string:
print(nome.upper())
print(nome.capitalize())

# list []
# lista de valores
# permitir diferentes tipos de dados na mesma lista

habilidades = ['python', 'Java', 'JavaScript']

print(habilidades[1])

for habilidade in habilidades:
    print(habilidade)

habilidades.append('HTML') #esse método APPEND irá adicionar no final da lista o html
habilidades.insert(1, "css") # esse adiciona em determinada posição
habilidades.remove('css')

print(habilidades)

#TUPLE ()
# "LISTA" de valores que não pode ser alterada: (sim, não, talvez)

opcoes = ('sim', 'nao', 'talvez')
raca_rpg = ('humano', 'elfo', 'orc')

def estatistica_notas(notas):
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    return maior, menor, media

notas = [10.0, 3.5, 7.8]
maior, menor, media = estatistica_notas(notas)
print(maior, menor, media)

# SET {}
# Conjunto de valores, não é indexado e permite elementos duplicados

habilidades = {'java', 'python'}
habilidades.add('Java')
print(habilidades)

for habilidade in habilidades:
    print(habilidade)


# DICT
# palavra -> definição
# chave -> valor
# key -> value

nome = 'Silvio'
idade = 89
patrimonio =2000000
altura = 1.7

pessoa = {
    'nome': 'Silvio',
    'idade': 89,
    'patrimonio': 2000000,
    'altura': 1.7
}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['patrimonio'])
print(pessoa['altura'])

#NONE 
# Variaveis que serão inicializadas em tempo de execução, retorno de função e parâmetros de função

nulo = None