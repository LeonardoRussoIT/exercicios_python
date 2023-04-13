'''
Crie um programa que leia o nome de uma pessoa e diga se 
ela tem "SILVA" no nome
'''

nome = input('Digite o nome: ')

# Primeiro deixando em maiúsculo, depois repatirmos, temos que fazer nessa ordem pois não da pra usar .upper() numa lista
print('SILVA' in nome.upper().split())