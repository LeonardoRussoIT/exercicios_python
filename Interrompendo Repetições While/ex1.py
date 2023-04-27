'''
Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 
999, que é a condição de parada. No final, mostre quantos 
números foram digitados e qual foi a soma entre elas 
(desconsiderando o flag).
'''

qnt_numeros = soma = 0

while True: # Loop infinito
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999: # Caso o numero analisado for igual a 999
        break # Encerra o loop
    else: # Do contrário
        qnt_numeros += 1
        soma += numero
        
print(f'A soma dos {qnt_numeros} valores foi {soma}!')