'''
Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário, com 15% de aumento.
'''

# Armazena o valor digitado pelo usuário dentro da variável salario e transforma em flutuante
salario = float(input('Qual é o salário do funcionário? R$'))

# Cria a variável novo_salario que armazena o salario + 15% de aumento
novo_salario = salario + (salario * 5 / 100) # -> fórmula de aumento -> valor + (valor * x / 100) sendo x o valor do aumento

# Imprime
print(f'Um funcionário que antes ganhava R${salario}, com 15% de aumento, passa a ganhar R${novo_salario:.2f}')