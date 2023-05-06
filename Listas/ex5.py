'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores 
pares e os valores ímpares digitados, respectivamente. Ao final, mostre 
o conteúdo das três listas geradas.
'''

valores = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor) # Adiciona o valor na lista valores com o método .append()
    
    if valor % 2 == 0: # Verifica se o valor é par -> se quando dividido por 2 o resto da divisão de 0
        pares.append(valor) # Adiciona o valor na lista de pares
    else: # Caso for ímpar
        impares.append(valor) # Adiciona na lista de impares

    continua = input('Quer continuar? [S/N] ').upper()
    if continua == 'N':
        break

print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')