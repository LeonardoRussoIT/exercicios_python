'''
Mostre a tabuada de um número que o usuário escolher utilizando um laço for.
'''

tabuada = int(input('Qual número você deseja ver a tabuada: '))

for contador in range(1, 11): # Percorra uma lista entre 1 e 11 (vai até o 10, último valor nunca conta)
    print(f'{tabuada} x {contador} = {tabuada * contador}') # -> tabuada x contador
