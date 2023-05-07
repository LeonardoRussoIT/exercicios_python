'''
Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores inteiros. Seu programa tem que analisar
todos os valores e dizer qual deles é o maior
'''

def maior(* numeros): # Função com desempacotamento, em que os parametros vão para uma tupla chamada numeros
    maior = contador = 0
    for numero in numeros:
        if contador == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
        print(numero, end=' ')
        contador += 1
    print(f'|| O maior é: {maior}')

maior(7, 5, 1, 2, 9, 3) # Como estamos desempacotando, não tem uma quantidade certa de parâmetros que podemos colocar
maior(2, 1, 5)
maior(1, 2)
maior(0, 1, 9, 2, 8)
maior(1)