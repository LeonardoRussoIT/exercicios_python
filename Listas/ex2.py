'''
Crie um programa onde o usuário possa digitar vários valores numéricos 
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não 
será adicionado. No final, serão exibidos todos os valores únicos 
digitados, em ordem crescente. 
'''

valores = [] # Cria uma lista vazia 

while True:
    valor = int(input('Digite um valor: '))
    if valor in valores: # Se o valor já estiver na lista valores
        print('Valor duplicado! Não vou adicionar...') 
    else: # Caso não tenha, adiciona o valor na lista
        valores.append(valor)

    continua = input('Quer continuar? [S/N] ').upper()
    if continua == 'N':
        break

print(f'Você digitou os valores {sorted(valores)}') # Coloca os valores em ordem crescente usando o método sorted()