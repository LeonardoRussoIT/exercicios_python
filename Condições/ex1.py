'''
Escreva um programa que faça o computador "pensar" em um
múmero inteiro entre 0 e 5 e peça pro usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu
'''

from random import randint

# Computador vai armazenar um valor entre 0 e 5 gerado aleatóriamente
computador = randint(0, 5)

# A variável jogador também vai armazenar um valor entre 0 e 5
jogador = int(input('Escolha um número entre 0 e 5: '))

if jogador == computador: # Caso o valor da variável jogador for igual ao da variável computador -> Imprima
    print(f'Você venceu! O computador também pensou no {jogador}')
else: # Do contrário / caso não seja -> imprima
    print(f'Você perdeu :( o computador pensou no número {computador}')