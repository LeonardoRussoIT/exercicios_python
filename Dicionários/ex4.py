'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando 
os dados de cada pessoa em um dicionário e todos os dicionários em uma 
lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

galera = []
pessoa = {}
idades = 0
while True:
    pessoa['nome'] = str(input('Nome: ')) # Adiciona um valor na chave nome
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0] # Joga tudo em maiúsculo e pega somente o primeiro elemento
        if pessoa['sexo'] in 'MF': # Verifica se o valor da chave sexo "está" em M ou F (verifica se o valor é M ou F)
            break
        print('Erro! Digite apenas M ou F') # Se o valor for diferente, pergunta o valor novamente
    pessoa['idade'] = int(input('Idade: '))
    idades += pessoa['idade']
    galera.append(pessoa.copy()) # Adiciona uma cópia do dicionário digitado
    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continua in 'SN':
            break
        print('Erro! Digite apenas S e N')
    if continua == 'N':
        break
print('-=-' * 20)
print(f'Ao todo temos {len(galera)} pessoas cadastradas') # Conta quantos dicionários tem na lista, ou seja, quantidade de pessoas
media = idades / len(galera)
print(f'A média de idade é de {media:.1f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera: # Percorre a lista
    if p['sexo'] == 'F': # Verifica se o valor da chave sexo é igual a F
        print(p['nome'], end=' ') # Imprime 
print()
print(f'Pessoas que estão acima da média de idade:')
for i in galera:
    if i['idade'] > media: # Mesma lógica que o loop de cima
        print(f'=> {i["nome"]}')