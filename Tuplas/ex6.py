'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais
'''

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratuito', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

# percorre cada palavra da tupla palavras
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    # percorre cada letra da palavra
    for letra in palavra:
        if letra.lower() in 'aeiou': # ->  verificamos se a letra é uma vogal usando a expressão letra.lower() in 'aeiou'
            print(letra, end=' ')