'''
Faça um programa que leia um número inteiro qualquer e mostre na
tela a sua tabuada.
'''

# Armazena o valor digitado pelo usuário dentro da variável numero e transforma em inteiro
numero = int(input('Digite um número: '))

print('-=' * 15)
print('Tabuada do', numero)
print('-=' * 15)

# Ao invés de criar uma variável, podemos fazer operções dentro mesmo das strings
print(f'{numero} x 1 = {numero * 1}')
print(f'{numero} x 2 = {numero * 2}')
print(f'{numero} x 3 = {numero * 3}')
print(f'{numero} x 4 = {numero * 4}')
print(f'{numero} x 5 = {numero * 5}')
print(f'{numero} x 6 = {numero * 6}')
print(f'{numero} x 7 = {numero * 7}')
print(f'{numero} x 8 = {numero * 8}')
print(f'{numero} x 9 = {numero * 9}')
print(f'{numero} x 10 = {numero * 10}')

