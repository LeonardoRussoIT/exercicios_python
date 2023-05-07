'''
Faça um programa que tenha uma função chamada contador(), que
recebe três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função 
criada:
a)De 1 até 10, de 1 em 1
b)De 10 até 0, de 2 em 2
c)Uma contagem personalizada
'''

def contador():
    for n in range(1, 11, 1): # Range começando do 1, indo até o 10, pulando de 1 em 1
        print(n, end=' ')
    print('FIM!')
    for n in range(10, -1, -2): # Range começando do 10, indo até 1, voltando de 2 em 2
        print(n, end=' ')
    print('FIM!')
    i = int(input('Início:')) # Recebe o início do range
    f = int(input('Fim: ')) + 1 # Fim do range mais 1 para ler o último número
    p = int(input('Passo: ')) # Passo que vai dar
    if i > f: # Se o início for maior que o fim, 
        p = -p # Transforma o passo em negativo
    elif p == 0: # Se o passo for 0
        p = 1 # Transforma o passo em 1
    for n in range(i, f, p): # Faz o loop com as informações dadas pelo teclado
        print(n, end=' ')
    print('FIM!')

contador() # Chama a função