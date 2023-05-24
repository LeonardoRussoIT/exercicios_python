'''
Crie um programa que leia dois números e mostre a soma entre eles.
'''

# Cria duas váriaveis, recebe o valor digitado pelo usuário e transforma os dados que ela receber em um inteiro usando o int()
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

# Cria uma variável que é a soma dos valores da variável numero1 e numero2
soma = numero1 + numero2

# Imprime usando f-strings
print(f'{numero1} + {numero2} = {soma}')