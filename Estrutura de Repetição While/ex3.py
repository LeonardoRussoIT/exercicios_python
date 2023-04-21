'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar            [ 4 ] novos números
[ 2 ] multiplicar      [ 5 ] sair do programa
[ 3 ] maior
Seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

opcao = 0 # Criando a variável opcao para o programa reconhecer que existe essa variável

while opcao != 5: # Loop só encerra quando a opção tiver valor 5
    opcao = int(input('''
    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos números
    [5] - sair do programa
    Sua escolha: 
    '''))
    print('-=-=-' * 10)
    if opcao == 1: # Se a opção for igual a 1
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opcao == 2: # Se não for, verifica se opção é igual a 2
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opcao == 3: # Se a opção for igual a 3
        if n1 > n2: # Verifica se o n1 é maior que n2
            print(f'{n1} é maior que {n2}')
        elif n2 > n1: # Se não for verifica se o n2 é maior que o n1
            print(f'{n1} é menor que {n2}')
        else: # Caso nenhuma verificação seja verdadeira
            print(f'{n1} e {n2} são iguais')
    elif opcao == 4: # Se não for, verifica se opção é igual a 4
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opcao == 5: # Se não for, verifica se opção é igual a 5
        print('Saindo do programa...')
    else: # Se nenhuma condição for verdadeira, (programa fecha)
        print('Opção inválida')
    print('-=-=-' * 10)