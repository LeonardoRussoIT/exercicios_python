'''
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

# Separa o nome é uma lista com índice
nome = input('Digite o seu nome: ').split()

# Acessa o índice 0, no caso o primeiro
print(f'Seu primeiro nome é {nome[0]}')

# Com números negativos, a contagem é de trás pra frente, sendo [-1] o primeiro índice a ser contado que é o último na contagem normal
print(f'Seu último nome é {nome[-1]}')