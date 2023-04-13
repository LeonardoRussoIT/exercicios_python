'''
Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.
'''

# Armazena o valor digitado pelo usuário dentro da variável real e transforma em flutuante
preco = float(input('Valor do produto: R$'))

# Cria a variável novo_preco que armazena o preço - 5% de desconto
novo_preco = preco - (preco * 5 / 100) # -> fórmula de desconto -> valor - (valor * x / 100) sendo x o valor do desconto

# Imprime
print(f'O produto que custava R${preco}, com desconto de 5%, vai passar a custar R${novo_preco:.2f}')