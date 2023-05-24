'''
Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

# Armazena o valor digitado pelo usuário dentro da variável algo 
algo = input('Digite algo: ')

# Imprime o tipo da variável
print('O tipo primitivo desse valor é', type(algo))

# Verifica se só tem espaços na variável
print('Só tem espaços?', algo.isspace())

# Só tem números
print('É um número?', algo.isnumeric())

# Só tem letras
print('É alfabético?', algo.isalpha())

# Possue letras e números
print('É alfanumérico?', algo.isalnum())

# Só tem letras maiúsculas
print('Está em maiúsculas?', algo.isupper())

# Só tem letras minúsculas
print('Está em minúsculas?', algo.islower())

# Todos os resultados são booleans, retornam somente: True ou False