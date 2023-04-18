"""
Escreva um programa para aprovar o empréstimo bancário para a 
compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo
será negado
"""

valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Seu salário: R$'))
anos = int(input('Em quantos anos você vai pagar a casa: '))

prestacao = valor_casa / (anos * 12) # quantidade de meses
minimo = salario * 30 / 100 # 30% do salário

if prestacao > minimo: # Verifica se a prestação é maior que o minímo exigido
    print('Empréstimo negado! Seu salário precisa ser maior')
else: # Se não for, faça isso
    print('Empréstimo Aprovado! Parabéns')