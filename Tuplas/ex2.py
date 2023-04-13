'''
Crie uma tupla preenchida com os 20 primeiros colocados do Brasileirão,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time do São Paulo.
'''
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 
         'Flamengo', 'Athletico Paranaense', 'Atlético Mineiro', 
         'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 
         'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético', 'Avaí', 'Juventude')

print('-=' * 15)
print('Tabela do Brasileirão 2022')

# Colocacao opcional
colocacao = 1

# Esse loop percorre a tupla "times" e gera os itens "time"
for time in times:
    print(f'{colocacao}º {time}')
    colocacao += 1
print('-=' * 15)

# times[:5] é a mesma coisa que times[0:5] -> print os itens do índice 0 até 5, 
print(f'Os 5 primeiros colocados são: {times[:5]}') 
print('-=' * 15)

# times[-4:] -> do índice -4 até -1
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 15)

# sorted é uma função que coloca os itens da tupla em ordem alfabética SEM ALTERAR A ORDEM DA "TUPLA ORIGINAL"
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)

# .index(elemento_que_deseja_procurar) retorna o índice/a posição do elemento
print(f'O São paulo está na {times.index("São Paulo") + 1}ª posição') # +1 só para corrigir, pois no python as contagens se iniciam no 0