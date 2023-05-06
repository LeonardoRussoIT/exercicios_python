'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois 
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso 
será guardado em um dicionário, incluindo o total de gols feitos durante 
o campeonato.
'''

jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
qnt_partidas = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
jogador['gols'] = []
for partida in range(qnt_partidas):
    gol = int(input(f'Quantos gols na partida {partida}? '))
    jogador['gols'].append(gol)
jogador['total'] = sum(jogador['gols'])
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 20)
print('{} jogou {} partidas'.format(jogador['nome'], qnt_partidas))
for p, g in enumerate(jogador['gols']):
    print(f' => Na partida {p}, fez {g} gols')