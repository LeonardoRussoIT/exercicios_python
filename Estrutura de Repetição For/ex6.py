'''
Desenvolva um programa que leia o primeiro termo e a razão de 
uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

razao = int(input('Qual é a razão da PA: '))
primeiro_termo = int(input('Qual é o primeiro termo dessa PA: '))
decimo = primeiro_termo + (10 - 1) * razao

for numeros in range(primeiro_termo, decimo + razao, razao):
    print(numeros, end=' ')