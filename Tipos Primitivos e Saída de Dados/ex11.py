'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo
que cada litro de tinta, pinta uma área de 2m².
'''

# Armazena o valor digitado pelo usuário dentro das variaveis altura e largura e transforma em número flutuante
altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

# Cria a variavel area que contém o produto dos valores de altura e largura
area = altura * largura

# Cria a variavel tinta com a area / 2 sabendo que cada litro de tinta pinta 2m² de parede
tinta = area / 2

# Imprime
print(f'A área da parede é {area}m²')
print(f'Para pintar essa parede, você precisara de {tinta:.1f}l de tinta')