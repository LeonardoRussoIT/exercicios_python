'''
Faça um programa que mostre a tabuada de vários números, um de 
cada vez, para cada valor digitado pelo usuário. O programa será 
interrompido quando o número solicitado for negativo. 
'''

while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('---' * 10)
    if tabuada < 0: # Se o valor da tabuada for menor que 0
        break # Encerre o loop
    for c in range(1,11):
        print(f'{tabuada} x {c} = {tabuada * c}')
    print('---' * 10)