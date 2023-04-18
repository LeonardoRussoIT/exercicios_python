'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Os dois valores são iguais
'''

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

if n1 > n2: # Verifica se o primeiro valor é maior que o segundo
    print('O primeiro valor é maior que o segundo!')
elif n2 > n1: # Verifica se o segundo valor é maior que o primeiro 
    print('O segundo valor é maior que o primeiro!')
else: # Se nenhuma das verificações forem verdadeiras, faça isso
    print('Os dois valores são iguais!')