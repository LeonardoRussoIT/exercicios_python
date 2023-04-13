'''
Crie um programa que leia um número Reak qualquer pelo teclado e 
mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''

numero = float(input('Digite um número: '))

# Transforma o numero em um inteiro, usando int(nome_da_variavel)
numero_inteiro = int(numero)

print(f'O valor digitado foi {numero} e a sua porção inteira é {numero_inteiro}')