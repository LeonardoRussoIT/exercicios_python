'''
Escreva um programa que converta uma temperatura digitada 
em °C e converta para °F.
'''

# Armazena o valor digitado pelo usuário dentro da variável temperatura_C e transforma em flutuante
temperatura_C = float(input('Informe a temperatura em °C: '))

# Transforma o valor da variável temperatura_C usando a fórmula de conversão de temperatura
temperatura_F = (temperatura_C * 9/5) + 32

# Imprime
print(f'{temperatura_C}°C é equivalente a {temperatura_F}°F')