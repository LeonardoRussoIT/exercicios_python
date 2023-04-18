
'''
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto    - em até 2x no cartão: preço formal
- à vista no cartão: 5% de desconto           - 3x ou mais no cartão: 20% de juros
'''

valor_compra = float(input('Valor total da compra: R$'))

print('''Escolha a forma de pagamento
[1] - à vista dinheiro / cheque
[2] - à vista cartão                   
[3] - 2x no cartão
[4] - 3x ou mais no cartão''')  # Utilizo o ''' ''' para o Python reconhecer as quebras de linha

opcao = input('Qual é a opção: ')

if opcao == '1': # Verifica se a opcao == '1'
    print(f'Sua compra que antes custava R${valor_compra:.2f} sairá por R${valor_compra - (valor_compra * 10 / 100):.2f}')
elif opcao == '2': # Verifica se a opcao == '2'
    print(f'Sua compra que antes custava R{valor_compra:.2f} sairá por R${valor_compra - (valor_compra * 5 / 100):.2f}')
elif opcao == '3': # Verifica se a opcao == '3'
    print(f'Sua compra será de 2 parcelas no valor de R${valor_compra / 2:.2f}')
elif opcao == '4': # Verifica se a opcao == '4'
    valor_compra = valor_compra + (valor_compra * 20 / 100) # Adicionando 20% no valor total
    qnt_parcelas = int(input('Em quando vezes você deseja parcelar a compra: '))
    print(f'Sua compra será de {qnt_parcelas} parcelas no valor de R${valor_compra / qnt_parcelas:.2f}')
    print(f'Ficando no total de R${valor_compra:.2f}')
else: # Se nenhuma condição for verdadeira
    print('Você não selecionou uma opção válida, programa fechando...')