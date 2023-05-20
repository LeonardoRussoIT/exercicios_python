'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma 
pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''


def voto(ano): # Cria função voto recebendo o parametro ano
    from datetime import date # Importa biblioteca datetime
    atual = date.today().year # atual recebe o ano atual (gerado pela biblioteca)
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos NÃO VOTA!' # Retorna
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o VOTO É OPCIONAL' # Retorna
    else:
        return f'Com {idade} anos o VOTO É OBRIGATÓRIO' # Retorna
    
print(voto(2000))
print(voto(2005))
print(voto(1956))