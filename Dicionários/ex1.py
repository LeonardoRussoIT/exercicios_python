'''
Faça um programa que leia nome e média de um aluno, guardando também 
a situação em um dicionário. No final, mostre o conteúdo da estrutura 
na tela.
'''

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['nota'] = float(input('Média do aluno: '))

if aluno['nota'] >= 6:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'


for k, v in aluno.items():
    print(f'{k} é igual a {v}')