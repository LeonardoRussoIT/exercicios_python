'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas 
respectivas posições na lista. 
'''

valores = []
maior = menor = 0

for indice in range(0, 5):
    valor = int(input(f'Digite um valor na posição {indice}: '))
    valores.append(valor) # Adiciona o valor com o método .append()

    if indice == 0:
        maior = menor = valor
    else:
        if maior < valor:
            maior = valor
        if menor > valor:
            menor = valor

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(valores): # Percorre toda a lista
    if valor == maior: # Se o valor verificado for igual ao maior
        print(f'{indice}...', end='') # mostre o índice
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(valores): # Percorre toda a lista
    if valor == menor: # Se o valor verificado for igual ao menor
        print(f'{indice}...', end='') # Mostre o índice
print()