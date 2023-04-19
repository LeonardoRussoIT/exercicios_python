'''
Crie um programa que mostre na tela todos os números pares 
que estão no intervalo entre 1 e 50
'''

for pares in range(0, 51, 2): # Percorra a lista de número de 0 até 50 pulando de 2 em 2 (pares)
    print(pares, end=' ') # end=' ' -> de um espaço ao invés de quebrar a linha