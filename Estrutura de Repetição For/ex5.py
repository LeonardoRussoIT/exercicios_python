'''
Desenvolva um programa que leia seis números inteiros e mostre 
a soma apenas daqueles que forem pares. Se o valor digitado for 
ímpar, desconsidere-o.
'''

soma_pares = 0 # Crio uma variável que irá armazenar a soma de todos os números pares digitados

for numeros in range(1, 7): # Percorra uma lista de 1 até 6 (último valor nunca é considerado)
    numero = int(input('Digite um número: ')) # Pergunte o número
    if numero % 2 == 0: # Verifica se quando o número for dividido por 2, o resto da divisão dê 0 (é par)
        soma_pares += numero # Atualiza o valor da soma_pares adicionando o numero

print(f'A soma de todos os números pares digitados é: {soma_pares}')