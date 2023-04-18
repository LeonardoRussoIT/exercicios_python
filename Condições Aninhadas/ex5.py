'''
A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento do atleta e mostre sua categoria, de 
acordo com a idade:
- Até 9 anos: mirim       Até 25 anos: sênior
- Até 14 anos: infantil   Acima: master
- Até 19 anos: júnior 
'''

from datetime import date # Importando função específica da biblioteca datetime
nascimento = int(input('Ano de nascimento: '))

idade = date.today().year - nascimento # date.today() -> pega a data do dia atual .year -> pega somente o ano

print(f'Tendo {idade} anos o jovem é considerado: ')

if idade <= 9: # Verifica se a idade é menor ou igual a 9
    print('Atleta mirim')
elif idade <= 14: # Verifica se a idade é menor ou igual a 14
    print('Atleta infantil')
elif idade <= 19: # Verifica se a idade é menor ou igual a 19
    print('Atleta júnior')
elif idade <= 25: # Verifica se a idade é menor ou igual a 25
    print('Atleta sênior')
else: # Caso nenhuma das condições sejam verdadeiras
    print('Atleta master')