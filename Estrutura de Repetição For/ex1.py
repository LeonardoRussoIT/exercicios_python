'''
Faça um programa que mostre na tela uma contagem regressiva para o 
estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 
segundo entre eles.
'''

from time import sleep # Importando a função sleep da biblioteca time

for count in range(10, -1, -1): # Percorra a lista de 10 até -1, dando um passo de -1
    print(count)
    sleep(1) # Espera 1 segundo para voltar pro loop novamente
print('BUM BUM POW POW')