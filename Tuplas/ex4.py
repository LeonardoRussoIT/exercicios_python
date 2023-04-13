'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em um tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posiçao foi digitado o primeiro valor 3.
c) Quais foram os números pares.
'''

# Criei 4 inputs, que ficarão armazenados dentro de uma tupla
num = (int(input('Digite um número: ')), 
       int(input('Digite mais número: ')), 
       int(input('Digite outro número: ')), 
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')

# .count(valor_que_deseja_ser_contado) -> nesse caso, quantas vezes o número 9, apareceu nessa tupla
print(f'O valor 9 apareceu {num.count(9)} vezes')

# se 3 estiver em número -> usei para evitar um erro caso o usuário não digite o número 3
if 3 in num:
    # .index(elemento_que_deseja_procurar) retorna o índice/a posição do elemento, uso o +1 para corrigir
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O usuário não digitou nenhum número 3')
    
print('Os números pares digitados foram: ',end='')
# analisa a tupla e se o número analisado for par, imprima
for n in num:
    if n%2 == 0:
        print(n, end=' ')