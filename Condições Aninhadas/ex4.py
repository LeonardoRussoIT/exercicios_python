'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5: reprovado
- média entre 5 e 6.9: recuperação
- média acima de 7: aprovado
'''

nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
media = (nota_1 + nota_2) / 2

print(f'Tirando {nota_1} e {nota_2} o aluno tem média de {media:.2f}')

if media < 5: # verifica se nota é menor do que 5
    print('Aluno REPROVADO')
elif media >= 5 and media <= 6.9: # verifica se a nota é maior que 5 E menor que 6.9
    print('Aluno de RECUPERAÇÃO')
else: # Caso nenhuma das afirmações sejam verdadeiras
    print('Aluno aprovado')