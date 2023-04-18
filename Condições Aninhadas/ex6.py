'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso    - 30 até 40: Obesidade
- Entre 18,5 e 25: Peso Ideal           - Acima de 40: Obesidade Mórbida
- 25 até 30: Sobrepeso
'''

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura ** 2) # ** -> elevado a 

print(f'O IMC dessa pessoa é {imc:.1f}')

if imc < 18.5: # Verifica se IMC é menor que 18.5
    print('Pessoa abaixo do peso ideal')
elif imc >= 18.5 and imc <= 25: # Caso não for, verifica se IMC é maior que 18.5 E menor ou igual que 25
    print('Pessoa com peso ideal')
elif imc > 25 and imc <= 30: # Caso não for, verifica se IMC é maior que 25 E menor que 30
    print('Pessoa com sobrepeso')
elif imc > 30 and imc <= 40: # Caso não for, verifica se IMC é maior que 30 E menor igual que 40
    print('Pessoa obesa')
else: # Caso nenhuma das afirmações sejam verdadeiras
    print('Pessoa com obesidade mórbida')