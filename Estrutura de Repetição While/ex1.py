'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = input('Informe seu sexo: [M/F] ').upper()

while sexo != 'M' and sexo != 'F': # Enquanto o valor de sexo for diferente de M e de F
    sexo = input('Opção inválida, digite novamente: ').upper() # Pergunte novamente o valor de sexo e faça a verificação novamente
    
print('Usuário cadastrado com sucesso...')