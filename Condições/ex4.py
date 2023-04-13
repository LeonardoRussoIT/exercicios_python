'''
Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 para viagens mais longas
'''

# Transforma em float para evitar erros na hora de multiplicar por um número flutuante
distancia = float(input('Qual é a distância da sua viagem? '))

if distancia <= 200: # Se a distancia for menor ou igual a 200, faça isso
    print(f'Você está prestes a começar uma viagem de {distancia}Km')
    print(F'E o preço da sua passagem será de R${distancia * 0.5:.2f}') # multiplica a distância por 0.5 e mostre somente 2 casas decimais
else: # Caso contrário (se a distância for maior que 200), faça isso
    print(f'Você está prestes a começar uma viagem de {distancia}Km')
    print(f'E o preço da sua passagem será de R${distancia * 0.45:.2f}') # mesma coisa do de cima mas multiplica por 0.45