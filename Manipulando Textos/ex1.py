'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
a) o nome com todas as letras maiúsculas e minúsculas
b) quantas letras tem ao todo (sem considerar os espaços)
c) quantas letras tem o primeiro nome
'''

nome = input('Seu nome completo: ')

# o método len() considera os espaços, então para corrigir usamos o métido .count(' ') para ter a quantidade de espaços e subtrair
qnt_letras = len(nome) - nome.count(' ')

# Parti o nome em índices, para poder acessar
nome_partido = nome.split()

# Método .upper() pra ficar tudo maiúsculo
print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}')

# Método .lower() pra ficar tudo maiúsculo
print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')

print(f'Seu nome tem: {qnt_letras} letras')

# Peguei o índice 0 da lista formada, que no caso é o primeiro nome
print(f'O seu primeiro nome é: {nome_partido[0]}')