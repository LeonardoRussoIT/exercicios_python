'''
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos Dólares ela pode comprar.
Considere US$1,00 = R$5,06.
'''

# Armazena o valor digitado pelo usuário dentro da variável real e transforma em flutuante
real = float(input('Quanto dinheiro você tem na carteira? R$'))

# Cria a variável dolar, armazenando o valor do real / por 5.06
dolar = real / 5.06

# Imprime
print(f'Com R${real} você pode comprar US${dolar:.2f}') # -> variavel:.2f mostra apenas 2 casas decimais