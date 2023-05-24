def formatar():
    preco.replace('.', ',')

def metade(valor):
    global preco
    preco = valor / 2
    return preco
    

def dobro(valor):
    preco = valor * 2
    return preco

def aumentar(valor):
    preco = valor + (valor * 10 / 100)
    return preco

def diminuir(valor):
    preco = valor - (valor * 15/100)
    return preco

def formatada(valor, moeda='R$'): # Adiciona como parâmetro a moeda, que sempre vai receber R$
    return f'{moeda}{valor:.2f}'.replace('.', ',') # .replace -> 1° o que vai ser trocado, 2° para o que vai ser trocado