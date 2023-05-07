'''
Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma 
entre todos os valores PARES sorteados pela função anterior
'''

from random import randint

sorteados = [] # Lista que vai conter os números sorteados

def sorteio():
    for c in range(0, 5):
        sorteados.append(randint(0, 10)) # Sorteando os números
    print(f'Sorteando 5 valores: {sorteados}')

def somaPar():
    soma_pares = 0
    for par in sorteados: # Varre e soma os que são pares
        if par % 2 == 0:
            soma_pares += par
    print(f'Somando os valores pares de {sorteados} temos: {soma_pares}')
    
sorteio()
somaPar()