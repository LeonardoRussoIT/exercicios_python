'''
Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso, de 0 até 6.
Seu programa deverá ler um número pelo teclado (entre 
0 e 6) e mostrá-lo por extenso.
'''

# Tupla contendo os números por extenso
numeros_extensos = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis'

# Criamos uma variável que vai armazenar a escolha do usuário, no formato int, para depois servir como índice na tupla
escolha = int(input('Escolha um número entre 0 e 6: ')) 

# "numero escolha" é o "numero por extenso" que está no índice "escolha"
numero_escolha = numeros_extensos[escolha]

# print
print(f'{escolha} por extenso é: {numero_escolha}') 