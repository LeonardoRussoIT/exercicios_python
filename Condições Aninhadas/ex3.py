'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo de alistamento. Seu 
programa também deverá mostrar o tempa que falta ou que passou do prazo
'''

from datetime import date

nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em 2023')

if idade < 18: # Verifica se a idade é maior que 18
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {nascimento + 18}')
elif idade == 18: # Verifica se a idade é igual a 18
    print(f'Você tem que se alistar IMEDIATAMENTE')
else: # Caso nenhuma das afirmações sejam verdadeiras
    print(f'Você deveria ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {nascimento + 18}')