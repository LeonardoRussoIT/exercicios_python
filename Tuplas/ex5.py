'''
Crie um programa que tenha uma tupla única com 
nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados
em forma tabular.
'''

listagem = ('Lápis', 1.75, 
            'Borracha', 2, 
            'Caderno', 15.90, 
            'Estojo', 25,
            'Transferidos', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-' * 40)

# Centraliza o títutlo entre 40 espaços de caracteres
print(f"{'LISTAGEM DE PREÇOS':^40}")

print('-' * 40)

# percorre a tupla
for posicao in range(0, len(listagem)):
    if posicao%2 == 0: # Se a posição for par (nesse caso toda posição par é o nome do produto)
        print(f'{listagem[posicao]:.<30}', end='') # imprima o nome do produto (.<30 -> adicione trinta caracteres da esquerda pra direita(nesse caso o .) até ter 30 espaços)
    else: # Se a posição for ímpar (os preços)
        print(f'R${listagem[posicao]:>7.2f}') # imprima os preços (adicionando 7.2 espaços da direita pra esquerda)
        