'''
Escreva um programa que pergunte o salário de um funcionário e 
calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%
'''

salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250: # Se o salário for menor ou igual a 1250
    aumento = salario + (salario * 15 / 100) # aumento é esse (15%)
else: # caso contrário (for maior que 1250)
    aumento = salario + (salario * 10 / 100) # aumento é esse (10%)
    
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora')