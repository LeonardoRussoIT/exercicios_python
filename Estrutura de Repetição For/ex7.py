'''
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade 
e quantas já são maiores.
'''

from datetime import date  # Importando a função date da biblioteca datetime

maior = 0 # Criando variável que vai armazenar o número de maiores
menor = 0 # Criando variável que vai armazenar o número de menores

for count in range(0 ,7): # Percorra o laço 7 vezes
    idade = int(input('Ano de nascimento: '))
    if date.today().year - idade >= 18: # Se o ano atual - o ano de nascimento for maior ou igual a 18
        maior += 1 # Atualiza a quantidade de maiores adicionando 1
    else:
        menor += 1 # Atualiza a quantidade de menores adicionando 1
        
print(f'Ao todo temos {maior} pessoas maiores de idade e {menor} menores de idade')