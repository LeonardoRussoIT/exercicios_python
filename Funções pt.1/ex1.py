'''
Faça um programa que tenha uma função chamada area(), que
receba as dimensões de um terreno retangular (largura e 
comprimento) e mostre a área do terreno
'''

def area(l, c): # Defini a função área com 2 parâmetros,l e c
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m²')

area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): '))) # Fiz a chamada da função, em que a e b são dois valores digitados pelo teclado