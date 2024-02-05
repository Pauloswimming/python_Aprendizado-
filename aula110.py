'''
175. groupby - agrupando valores (itertools) #agrupar os valores 
ele explica logica
'''
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def orderna(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos,key=orderna)
grupos = groupby(alunos_agrupados,key=orderna)

for chave,grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)