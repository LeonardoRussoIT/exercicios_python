'''
Faça um programa que calcule a soma entre todos os números 
que são múltiplos de três e que se encontram no intervalo 
de 1 até 500.
'''

soma_impares = 0 # Cria uma variável vazia que vai adicionando as somas dos ímpares
qnt_impares = 0 # Cria uma variável vazia que vai servir como contador para a quantidade de ímpares

for impar in range(1, 500, 2): # Percorra a lista de números entre 1 até 500 pulando de 2 em 2 (somente os ímpares)
    if impar % 3 == 0: # Se o número verificado, quando divido por 3 o resto dê 0 (múltiplo de 3)
        qnt_impares += 1 # Adiciona mais um na quantidade de ímpares
        soma_impares += impar # Atualiza a soma dos ímpares adicionando o ímpar múltiplo de três

print(f'A soma dos {qnt_impares} números é {soma_impares}')