'''
Escreva um programa que pergunte a quantidade de km
percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado.
'''

# Armazena o valor digitado pelo usuário dentro das variaveis dias e kms e transforma em número inteiro
dias = int(input('Quantos dias alugados? '))
kms = int(input('Quantos Km rodados? '))

# Cria a variável total, que contém a experessão matemática abaixo
total = (dias * 60) + (kms * 0.15)

# Imprime
print(f'O total a pagar é de R${total:.2f}')