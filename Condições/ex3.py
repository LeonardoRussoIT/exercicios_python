'''
Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR
'''

numero = int(input('Digite um número: '))

# le-se "Se quando o valor de numero for dividido por 2, o resto dessa divisão de 0" -> significa que o número é par
if numero % 2 == 0: # Se for verdadeira essa sentença, faça isso
    print(f'O número {numero} é par!')
else: # Se o if acima for falso, faça isso
    print(f'O número {numero} é ímpar!')