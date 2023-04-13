'''
Faça um programa que leia o nome de uma pessoa e mostre
uma mensagem de boas-vindas.
'''

# Cria a variável nome que vai armazenar o valor digitado pelo usuário
nome = input('Seu nome? ')

# f'' -> f-string serve para colocar variáveis dentro de uma string ao invés de concatenar
print(f'Bem Vindo, {nome}')