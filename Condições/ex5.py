'''
Faça um programa que leia um ano qualquer
e mostre se ele é BISSEXTO
'''

# Para verificar se um ano é bissexto temos que conferir se ele:
# quando dividido por 4 der uma divisão inteira (não ter resto)
# quando dividido por 100 não der um número inteiro
# quando dividido ´por 400 dê um número inteiro

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

# Para ser considerado verdadeiro, precisa passar por essas três condições!
# and -> as duas condições devem ser verdadeiras
# or -> ou uma ou outra tem que ser verdadeira
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # caso seja verdadeiro -> execute
    print(f'O ano {ano} é BISSEXTO')
else: # Não é verdade, imprima
    print(f'O ano {ano} NÃO é BISSEXTO')