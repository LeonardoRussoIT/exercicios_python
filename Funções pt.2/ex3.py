'''
Crie um programa que tenha a função leiaInt(), que vai funcionar 
de forma semelhante 'a função input() do Python, só que fazendo 
a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''

def leiaint(txt): # Crio um parâmetro aleatório só para receber na chamada da função
    global logica # Torna a variável logica como uma variável de escopo global
    logica = '' # Variável vazia que vai armazenar True ou False para encerrar o loop
    while logica != True:
        a = str(input(txt)) # Recebe o valor do parâmetro txt e transforma em string ->
        if a.isnumeric(): # Para validar se é um valor numérico ou não
            logica = True # Lógica se torna True
            return a # Retorna o valor numérico na variável n
        else: 
            print('Digite um número válido')
            logica = False


n = leiaint('Digite um número:')
print(f'Você digitou o número {n}')