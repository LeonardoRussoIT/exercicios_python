'''
Faça um programa que tenha uma função notas() que pode receber várias 
notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def notas(*n, situacao=False):
    '''
    *n : lista que vai armazenar os parâmetros passados (não importa a quantidade)
    sit : parâmetro opcional, se ele for passado como verdadeiro ele mostra a situação do aluno
    Essa função irá mostrar: Quantidade de notas, maior, menor, média, situação (opcional)
    '''
    r = dict()
    r['quantidade de notas'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if situacao == True:
        if r['média'] >= 6:
            r['situação'] = 'Boa'
        else:
            r['situação'] = 'Ruim'
        
    return r 

resposta = notas(9.5, 5.5, 3, 8.75, 8.5, 10, 2.5, situacao=True)
print(resposta)