'''
Faça um programa que leia nome e peso de várias pessoas, 
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

pessoas = [] # Duas listas vazias que irão armazenar dados, sendo que PESSOA vai ser só temporário
pessoa = []
qnt_pessoas = maior_peso = menor_peso = 0

while True:
    pessoa.append(str(input('Nome: '))) # Adiciono o nome
    pessoa.append(float(input('Peso: '))) # Adiciono peso
    qnt_pessoas += 1
    if qnt_pessoas == 1: # A primeira pessoa tem o maior peso e menor peso
        maior_peso = pessoa[1] # Repare que eu faço essa verificação na lista temporária PESSOA
        menor_peso = pessoa[1]
    else: # Aqui já faz a verificação nas outras informações que vierem
        if maior_peso < pessoa[1]: # pessoa[1] -> é o peso, na lista PESSOA
            maior_peso = pessoa[1]
        if menor_peso > pessoa[1]:
            menor_peso = pessoa[1]
    pessoas.append(pessoa[:]) # Adiciona uma cópia de pessoa [:] -> sem fazer uma ligação entre elas
    pessoa.clear() # Esvazio a lista pessoa para fazer uma outra verificação
    
    continua = str(input('Quer continuar? [S/N] ')).lower()
    if continua == 'n':
        break
        
print(f'Ao todo você cadastrou {qnt_pessoas} pessoas')
print(f'O maior peso foi de {maior_peso}Kg ', end='')
for p in pessoas: # Percorro a lista principal PESSOAS
    if p[1] == maior_peso: # Se o elemento p[1] (peso) for igual ao maior peso
        print(f'[{p[0]}]', end=' ') # Imprima o nome dessa pessoa (p[0])
print()
print(f'O menor peso foi de {menor_peso}Kg', end=' ')
for p in pessoas: # Mesma lógica que o loop de cima
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')
print()