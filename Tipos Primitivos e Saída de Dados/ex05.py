'''
Faça um programa que leia um número inteiro e mostre na tela
o seu sucessor e seu antecessor.
'''
# Armazena o valor digitado pelo usuário dentro da variável numero e transforma em inteiro
numero = int(input('Digite um número: '))

antecessor = numero - 1 # Cria a variável antecessor, armazenando o valor anterior da variável numero
sucessor = numero + 1 # Cria a variável sucessor, armazenando o valor posterior da variável numero

# Imprime
print(f'O sucessor de {numero} é {sucessor}')
print(f'O antecessor de {numero} é {antecessor}')