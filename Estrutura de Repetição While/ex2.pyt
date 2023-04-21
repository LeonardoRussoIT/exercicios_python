'''
Melhore o jogo onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer.
'''

from random import randint

computador = randint(0, 10)

print('O computador pensou em um número entre 0 e 10, você consegue adivinhar?')
jogador = int(input('Seu palpite: '))

while computador != jogador: # Enquanto o valor do computador for diferente do valor do jogador
    jogador = int(input('Errou, tente novamente: ')) # Pergunte novamente o valor de jogador e faça um nova verificação
    
print(f'Parabéns, você acertou! O número pensado foi {computador}')