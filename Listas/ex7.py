'''
Crie um programa onde o usuário possa digitar sete valores 
numéricos e cadastre-os em uma lista única que mantenha 
separados os valores pares e ímpares. No final, mostre os 
valores pares e ímpares em ordem crescente.
'''

numeros = [[], []]

valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores impares digitados foram {numeros[1]}')