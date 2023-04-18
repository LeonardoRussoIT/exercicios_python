'''Crie um programa que faça o computador jogar JOKENPÔ com você'''

from random import randint # Importa a função randint da biblioteca random

jogadas = ['pedra', 'papel', 'tesoura'] # Cria uma lista com as jogadas

humano = int(input('''Selecione a sua jogada 
[1] - pedra
[2] - papel
[3] - tesoura
''')) # Usei ''' ''' para o Python considerar as quebras de linha

jogada_humano = jogadas[humano - 1] # jogada_humano é o item do índice que o humando escolheu, -1 para corrigir   
jogada_computador = jogadas[randint(0,2)] # jogada_computador é o item do índice gerado aleatóriamente

print(f'Você jogou {jogada_humano} e o computador jogou {jogada_computador}')

if jogada_computador == 'pedra': # Se o computador jogou pedra 
    if jogada_humano == 'pedra': # Verifica se o humano jogou pedra também
        print('Empate!')
    elif jogada_humano == 'tesoura': # Verifica se o humano jogou tesoura
        print('Perdeu!')
    elif jogada_humano == 'papel': # Verifica se o humano jogou papel
        print('Ganhou!')
elif jogada_computador == 'papel': # Se o computador jogou papel 
    if jogada_humano == 'pedra': # Verifica se o humano jogou pedra
        print('Perdeu!')
    elif jogada_humano == 'papel': # Verifica se o humano jogou papel também
        print('Empate!')
    elif jogada_humano == 'tesoura': # Verifica se o humano jogou tesoura 
        print('Ganhou!')    
elif jogada_computador == 'tesoura': # Se o computador jogou tesoura 
    if jogada_humano == 'pedra':  # Verifica se o humano jogou pedra
        print('Ganhou!')
    elif jogada_humano == 'papel': # Verifica se o humano jogou papel
        print('Perdeu!')
    elif jogada_humano == 'tesoura': # Verifica se o humano jogou tesoura também
        print('Empate!')
