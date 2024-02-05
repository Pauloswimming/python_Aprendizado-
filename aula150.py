# Context Manager com função - Criando e Usando gerenciadores de contexto
'''
242. Context Manager com contextlib.contextmanager
'''
from contextlib import contextmanager

@contextmanager

def my_open(caminho_arquivo,modo):
    try:
        print('abrindo arquivo')
        arquivo = open(caminho_arquivo,modo,encoding="utf8")
        yield arquivo #transforma em um generator não em uma função 
    except Exception as e:
        print('ocorreu erro',e)
    finally:
        print('fechando arquivo')
        arquivo.close()

with my_open('aula150.txt','w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n',123)
    arquivo.write('linha 3\n')
    print('WITH',arquivo)