'''
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o 
usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
'''

mulheres_menor_20 = homens = pessoas_maior_18 = 0

while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper()
    print('---' * 10)
    continua = input('Deseja continuar? [S/N] ').upper()
    print('---' * 10)
    if idade > 18: # Verifica se idade é menor que 18
        pessoas_maior_18 += 1 # Adiciona +1 na variavel
    if sexo == 'M': # Verifica se o sexo é masculino
        homens += 1 # Adiciona +1 na variavel
    if sexo == 'F' and idade < 20: # Verifica se o sexo é feminino e a idade é menor que 20
        mulheres_menor_20 += 1 # Adiciona +1 na variavel
    if continua == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {pessoas_maior_18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menor_20} mulheres com menos de 20 anos')