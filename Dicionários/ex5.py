'''
Aprimore o exercício 3 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador
'''

jogadores = []
jogador = {}

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partida'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    for c in range(jogador['partida']):
        gol = int(input(f'    Quantos gols na partida {c + 1} '))
        jogador['gols'].append(gol)
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continua in 'SN':
            break
        print('Erro! Digite apenas S e N')
    if continua == 'N':
        break
print(jogadores)

##### FALTA TERMINAR #####