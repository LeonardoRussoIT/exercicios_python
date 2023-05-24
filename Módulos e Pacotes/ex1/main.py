'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). Faça também um programa 
que importe esse módulo e use algumas dessas funções.
'''

import moeda # Importando módulo criado

p = float(input('Digite o preço: R$'))

print(f'A metade de R${p} é R${moeda.metade(p)}') # Fazendo a chamada -> 1° nome do módulo e depois função
print(f'O dobro de R${p} é R${moeda.dobro(p)}') # Fazendo a chamada -> 1° nome do módulo e depois função
print(f'Aumentando R${p} em 10% temos R${moeda.aumentar(p)}') # Fazendo a chamada -> 1° nome do módulo e depois função
print(f'Diminuindo R${p} em 15% temos R${moeda.diminuir(p)}') # Fazendo a chamada -> 1° nome do módulo e depois função