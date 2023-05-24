'''
Adapte o código do exercício 1, criando uma função adicional 
chamada moeda() que consiga mostrar os números como um valor 
monetário formatado.
'''

import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.formatada(p)} é {moeda.formatada(moeda.metade(p))}') # Passa como parâmetro a própria função
print(f'O dobro de {moeda.formatada(p)} é {moeda.formatada(moeda.dobro(p))}') # Passa como parâmetro a própria função
print(f'Aumentando {moeda.formatada(p)} em 10% temos {moeda.formatada(moeda.aumentar(p))}') # Passa como parâmetro a própria função
print(f'Diminuindo {moeda.formatada(p)} em 15% temos {moeda.formatada(moeda.diminuir(p))}') # Passa como parâmetro a própria função