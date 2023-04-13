'''
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
'''

# Armazena o valor digitado pelo usuário dentro das variaveis nota1 e nota2 e transforma em número flutuante
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

# Cria a variável valor e armazena a média aritimética das notas
media = (nota1 + nota2) / 2

# Imprime
print(f'A média de notas é: {media}')