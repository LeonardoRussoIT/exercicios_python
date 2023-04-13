'''
Faça um programa que leia uma frase pelo teclado e mostre:
a) Quantas vezes apareceu a letra "A"
b) Em que posição ela aparece a primeira vez
c) Em que posição ela aparece a última vez
'''

# Transforma tudo em maiúscula e retira os espaços do início e fim pra evitar erro
frase = input('Digite uma frase: ').upper().strip()

# .count('A') -> pra contar a quantidade de As
print('A letra "A" apareceu {} vezes'.format(frase.count('A')))

# .find() -> método que mostra a primeira posição em que o elemento está (+1 pra corrigir pois a contagem começa no 0)
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A') + 1))

# .rfint() -> mesma função do find mas começa a contar da direita
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A') + 1))