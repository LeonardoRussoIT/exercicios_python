'''
Crie um programa onde o usuário possa digitar cinco valores numéricos 
e cadastre-os em uma lista, já na posição correta de inserção (sem usar 
o sort()). No final, mostre a lista ordenada na tela.
'''

import bisect # Importando a biblioteca bisect

valores = []

for indice in range(5):
    valor = int(input('Digite um valor: '))
    bisect.insort(valores, valor) # O método insort insere o valor já de forma ordenada -> lê-se "Na lista valores, adiciona valor"
    print(f'Número {valor} inserido na posição {valores.index(valor)}') # A função .index indica em qual índice está o valor

print(f'Números digitados {valores}')