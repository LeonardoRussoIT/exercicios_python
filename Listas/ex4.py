'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

valores = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor) # Adiciona o valor na lista valores


    continua = input('Quer continuar? [S/N] ').upper()
    if continua == 'N':
        break

print(f'Você digitou {len(valores)} elementos') # Mostra a quantidade de elementos que tem na lista
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}') # sorted(lista, reverse=True) -> mostra a lista ordenada de forma decrescente
if 5 in valores: # Verifica se o valor 5 está na lista valores
    print('O valor 5 faz parte da lista!')
else: # Caso não esteja
    print('O valor 5 não foi encontrado na lista')