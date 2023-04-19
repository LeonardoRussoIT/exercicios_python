'''
Faça um programa que leia o peso de cinco pessoas. No final, 
mostre qual foi o maior e o menor peso lidos.
'''

lista = [] # Cria uma lista fazia que vai armazenar os pesos

for pessoa in range(0, 5): # Laço que vai repetir 5 vezes
    peso = float(input(f'Peso da pessoa {pessoa + 1}: ')) # pessoa + 1 para corrigir a contagem que começa no 0
    lista += [peso] # Adiciona o peso na lista (lista recebe lista + peso)
    
print(f'O maior peso registrado foi {max(lista)}kg e o menor foi {min(lista)}kg') # max(lista) -> maior valor da lista; min(lista) -> menor valor da lista