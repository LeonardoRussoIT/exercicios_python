'''
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
'''

total = produto_maior_mil = valor_produto_mais_barato = contador = 0 # Criei a variável contador só para conseguir definir que o produto mais barato é o primeiro
produto_mais_barato = ''

while True:
    produto = input('Nome do produto: ')
    valor_produto = float(input('Preço: R$'))
    continua = input('Quer continuar? [S/N] ').upper()
    print('---' * 10)
    contador += 1
    total += valor_produto
    if valor_produto > 1000:
        produto_maior_mil += 1
    if contador == 1: # O primeiro produto é o mais barato
        valor_produto_mais_barato = valor_produto
        produto_mais_barato = produto
    else: # Já no segundo loop ele sempre vai fazer essa verificação para ver se precisa atualizar
        if valor_produto_mais_barato > valor_produto:
            valor_produto_mais_barato = valor_produto
            produto_mais_barato = produto
    if continua == 'N': # Se o valor de continua for igual a N
        print('Fim do programa...')
        break # Encerra o loop

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produto_maior_mil} produtos custando mais que R$1000.00')
print(f'O produto mais barato foi {produto_mais_barato} que custa R${valor_produto_mais_barato:.2f}')