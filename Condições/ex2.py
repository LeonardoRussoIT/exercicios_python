'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem 
dizendo que ele foi multado
A multa vai custar R$7,00 para cada Km acima do limite
'''

velocidade = int(input('Qual é a velocidade atual do carro? '))

# Conta pra saber a velocidade acima do permitido
velocidade_acima = velocidade - 80

# Multiplica por 7 a quantidade de kms acima do permitido para saber o valor da multa
valor_da_multa = velocidade_acima * 7

if velocidade > 80: # Verifica se a velocidade é acima de 80, se for, faça isso
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h')
    print(f'Valor da multa é de {valor_da_multa:.2f}')
else: # Do contrário, faça isso
    print('Tenha um bom dia! Dirija com segurança')