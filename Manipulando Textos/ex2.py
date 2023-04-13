'''
Crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome "SANTO"
'''

# Utilizei o método strip() para retirar os espaços no ínicio para previnir possível erro
cidade = input('Digite o nome da cidade: ').strip()

# Primeiro deixando em maiúsculo, depois repatirmos, temos que fazer nessa ordem pois não da pra usar .upper() numa lista
# Como a palavra SANTO tem 5 letras, fazemos a verificação, analise somente os 5 primeiros caracteres -> de 0 a 5
print('SANTO' in cidade[0:5].upper().split())