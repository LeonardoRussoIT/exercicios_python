'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
'''

# Armazena o valor digitado pelo usuário dentro da variável numero e transforma em inteiro
numero = int(input('Digite um número: '))

# Cria a variável dobro e armazena o dobro da variável numero
dobro = numero * 2

# Cria a variável triplo e armazena o triplo da variável numero
triplo = numero * 3

# Cria a variável raiz_quadrada e armazena a raiz quadrada da variável numero
raiz_quadrada = numero ** (1/2) # -> fórmula da raiz quadrada em Python

# Imprime
print(f'O dobro de {numero} é: {dobro}')
print(f'O triplo de {numero} é: {triplo}')
print(f'A raiz quadrada de {numero} é: {raiz_quadrada:.2f}')