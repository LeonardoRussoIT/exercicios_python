'''
Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um 
jogador e quantos gols ele marcou. O programa deverá 
ser capaz de mostrar a ficha do jogador, mesmo que 
algum dado não tenha sido informado corretamente.
'''

def ficha(nome='', gols=0):
    if nome == '': # faz a verificação se o nome esta vazio
        nome = '<desconhecido>'
    if gols.isnumeric(): # Verifica se o número de gols é um valor numérico (só funciona em str)
        gols = int(gols) # Caso seja transfoma em inteiro
    else: # Se não for é == 0
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')
    
nome = str(input('Qual o nome do jogador? '))
gols = str(input('Número de gols: '))
ficha(nome, gols)