'''
Faça um programa que jogue par ou ímpar com o computador. O jogo 
só será interrompido quando o jogador perder, mostrando o total 
de vitórias consecutivas que ele conquistou no final do jogo. 
'''

from random import randint
vitoria = 0

while True:
    computador = randint(0,10)
    jogador = int(input('Escolha um valor: '))
    escolha = input('Par ou Ímpar [P/I] ').upper()
    resultado = jogador + computador
    print('---' * 10)
    if escolha == 'P': # Se o jogador escolheu par
        if resultado % 2 == 0: # Se a jogada der par, jogador venceu
            print(f'O computador jogou {computador} e você {jogador}, DEU PAR. Você ganhou!')
            vitoria += 1
        else: # Se der impar, jogador perdeu
            print(f'O computador jogou {computador} e você {jogador}, DEU ÍMPAR. Você perdeu!')
            break # Encerra o loop
    if escolha == 'I': # Se o jogador escolheu impar
        if resultado % 2 == 0: # E a jogada deu par, jogador perdeu
            print(f'O computador jogou {computador} e você {jogador}, DEU PAR. Você perdeu!')
            break # Encerra o loop
        else: # Se der ímpar, jogador venceu
            print(f'O computador jogou {computador} e você {jogador}, DEU ÍMPAR. Você ganhou!')
            vitoria += 1
    print('---' * 10)

print('---' * 10)
print(f'Game Over! Você venceu {vitoria} vezes')