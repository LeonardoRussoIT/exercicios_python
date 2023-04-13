'''
Escreva um programa que leia um valor em metros e 
exiba convertido em centímetros e milímetros.
'''

# Armazena o valor digitado pelo usuário dentro da metros e transforma em número flutuante
metros = float(input('Medida em metros: '))

# Cria a variável centimetros e armazena o centimetros do valor digitado em metros
centimetros = metros * 100

# Cria a variável centimetros e armazena o milímetros do valor digitado em metros
milimetros = metros * 1000

# Imprime
print(f'{metros}m é equivalente a {centimetros}cm')
print(f'{metros}m é equivalente a {milimetros}mm')