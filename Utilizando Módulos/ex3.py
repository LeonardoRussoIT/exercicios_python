'''O professor quer sortear um dos seus quatro alunos 
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido'''

# Importei a runção randint da biblioteca random
from random import randint

# Crie uma tupla com os 4 nomes armazenados por meio de inputs
nomes = (input('Primeiro nome: '), input('Segundo nome: '), input('Terceiro nome: '), input('Quarto nome: '))

# Sorteei um número entre 0 e 3, que equivale os índices da tupla
sorteado = randint(0, 3)

# Imprime -> nome no indice sorteado
print(f'O aluno sorteado foi: {nomes[sorteado]}')