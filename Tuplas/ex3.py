'''
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
'''
# importo somente o método de randomizar um número inteiro (randint)
from random import randint

# Sorteando 5 valores entre 0 e 10
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print('Os valores sorteados foram: ', end='') # -> end='' foi usado para imprimir todos os números na mesma linha, separados apenas por um espaço vazio, por padrão ao final do print, é gerada uma nova linha /n

# percorra "numeros" e imprime cada um dos números
for n in numeros:
    print(f'{n} ', end='')

# método max() e min() verifica qual é o maior e o menor valor gerado
print(f'\nO maior valor sorteado foi {max(numeros)}') # \n para dar uma quebra de linha
print(f'O menor valor sorteado foi {min(numeros)}')