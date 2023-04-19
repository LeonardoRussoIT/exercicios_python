'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

idade_mais_velho = 0 # Criei a variável para armazenar a idade do homem mais velho
homem_mais_velho = '' # String vazia para armazenar o nome do homem mais velho
soma_idades = 0 # Variável para ir adicionando a soma das idades das pessoas
mulheres_menor_20 = 0 # Variável para armazenar a quantidade de mulheres com menos de 20 anos

for pessoas in range(0, 4): # Laço percorrendo 4 vezes
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sexo = input('Seu sexo: [m] ou [f] ').lower()
    soma_idades += idade # Adiciona a idade na variável soma das idades
    if pessoas == 0: # Essa condição só funciona uma vez, a pessoa mais velha é a primeira
        idade_mais_velho = idade
        homem_mais_velho = nome
    if sexo == 'm' and idade > idade_mais_velho: # Se for homem e a idade for mais alta
        idade_mais_velho = idade # idade do mais velho passa a ser essa idade
        homem_mais_velho = nome # nome do mais velho passa a ser o nome
    if sexo == 'f' and idade < 20: # Se for mulher com idade menor que 20s
        mulheres_menor_20 += 1 # Adiciona 1 na variável
            
media_do_grupo = soma_idades / 4

print(f'A média de idade do grupo é {media_do_grupo:.0f} anos')
print(f'O homem mais velho se chama {homem_mais_velho}')
print(f'Temos {mulheres_menor_20} mulheres com menos de 20 anos')