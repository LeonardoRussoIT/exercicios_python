'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for 
diferente de ZERO, o dicionário receberá também o ano de contratação e o 
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa 
vai se aposentar.
'''

trabalhador = {}

trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = int(input('Idade: '))
trabalhador['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação'))
    trabalhador['salário'] = float(input('Salário: R$'))
print('-=-' * 20)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')