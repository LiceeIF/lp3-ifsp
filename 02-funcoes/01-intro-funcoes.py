# FUNÇÃO
# feita para modularizar o programa, quando temos função, é costume ter reuso e manutenabilidade 

# DECLARAÇÃO
# def nome_funcao(parametros):
#    corpo_da_funcao

#e.g.:
# só pode acessar dentre as 8h e 18h, saida se está dentro ou não do horário comercial
hora_atual = 12

# o que em if seria
if hora_atual >= 8 and hora_atual <= 18:
    print('permitido o acesso')

# em uma função, seria:
def dentro_horario_comercial(hora_atual):
    return hora_atual >= 8 and hora_atual <= 18



# FUNÇÃO SEM RETORNO
#função sem retorno sempre tem um side effect = efeito colateral.
def diga_ola(nome):
    print(f'ola {nome}')
# ->
# chamada
diga_ola('Joao')


# FUNÇÃO COM RETORNO
#função sem side effect é chamada de função pura
def montar_frase(nome):
    return f'Olá {nome}'

nome = 'João'
print(montar_frase(nome))

# PARÂMETROS E ARGUMENTOS
#parâmetros são referências que podem ser acessadas dentro da função
# argumentos são os valores passados para os parâmetros

def somar(num1, num2):
    return num1 + num2

somar(10.0, 5.0)


#ESCOPO DE VARIAVEIS
# VARIAVEL LOCAL
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media
#print media


# VARIAVEL GLOBAL
total = 0.0

def soma(n1, n2, n3):
    total = n1 + n2 + n3
    return total

print(total)
soma(1,3,5)
print(total)

# PARAMETROS COM VALOR PADRÃO (default)
def gerar_boas_vindas(mensagem,nome):
    return f'{mensagem}, {nome}'
print(gerar_boas_vindas('bom dia', 'Maria'))
print(gerar_boas_vindas('bom dia', 'Rodrigo Baesa'))

def boas_vindas(nome, mensagem = 'bom dia'): #QUANDO O VALOR É PADRÃO, VOCE PRECISA DEIXÁ-LO EM PRIMEIRA ORDEM
    return f'{mensagem}, {nome}'
print(boas_vindas(nome='Maria'))

#ARGUMENTOS NOMEADOS
print(boas_vindas(nome='Maria'))

# DOCSTRINGS
# comentário de documentação
def somar(n1,n2):
    '''

    return: soma dos números
    '''
    return n1+n2

# FUNCÕES BULT-IN
# print, type, sum, len, max, min

