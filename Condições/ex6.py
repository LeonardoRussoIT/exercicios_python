'''
Faça um programa que leia três números e 
mostre qual é o maior e qual é o menor
'''

primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
terceiro = int(input('Terceiro número: '))

# Como o único número digitado até então é o primeiro, o primeiro é o maior número e o menor número
menor = primeiro
if segundo < primeiro and segundo < terceiro: # caso o segundo for menor que o primeiro (que é o menor por enquanto) ***E*** for menor que o terceiro também
    menor = segundo # o menor valor passa a ser o segundo
if terceiro < primeiro and terceiro < segundo: # se o terceiro for menor que o primeiro e menor que o segundo
    menor = terceiro # menor valor passa a ser o terceiro
    
maior = primeiro # Maior valor é o primeiro
if segundo > primeiro and segundo > terceiro: # Se o segundo for maior que o primeiro e o terceiro
    maior = segundo # maior passa a ser o segundo
if terceiro > primeiro and terceiro > segundo: # Se o terceiro for maior que o segundo e o primeiro
    maior = terceiro # maior passa a ser o terceiro

print(f'O maior número digitado é o {maior}')
print(f'O menor número digitado é o {menor}')