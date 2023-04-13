'''
O mesmo professor do desafio anterior quer sortear a ordem
de apresentação de trabalho dos alunos. Faça um programa 
que leia o nome dos quatro alunos e mostre a ordem sorteada
'''

# Importei toda a biblioteca random
import random

#OBS -> tem que ser em uma lista pois a tupla *é imutável*

# Criei a lista contendo os nomes obtidos por meio de input
lista = [input('Primeiro nome: '), input('Segundo nome: '), input('Terceiro nome: '), input('Quarto nome: ')]

# Usei o método shuffle para "embaralhar" a ordem das strings da lista
random.shuffle(lista)

# Imprime
print(lista)