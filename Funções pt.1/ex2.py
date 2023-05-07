'''
Faça um programa que tenha uma função chamda escreva(), que
receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanha adaptável.
ex:
escreva('Olá, Mundo!')
saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
'''

def escreva(palavra): # Crio uma função chamada escreva com um parâmetro palavra
    print('=' * len(palavra)) # A linha de cima vai ter o len da palavra naquele caso * =
    print(palavra) 
    print('=' * len(palavra)) # A linha de baixo vai ter o len da palavra naquele caso * = 


escreva(' Leonardo ')
escreva(' Simões ')
escreva(' PYTHON ')
escreva(' EU AMO PROGRAMAÇÃO ')