'''
Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre
o comprimento da hipotenusa
'''

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateo adjacente: '))

# Utilizo a fórmula da hipotenusa para descobrir o valor
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) # ** X -> elevado a X

print(f'A hipotenusa vai medir {hipotenusa:.2f}')