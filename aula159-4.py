'''
268. Configurações do decorator dataclass
'''
from dataclasses import asdict, astuple, dataclass


@dataclass

class Pessoa:
    nome:str
    sobrenome:str

if __name__ == '__main__':
    lista = [Pessoa('A','Z'),Pessoa('B','X'),Pessoa('C','Y')]
    ordenadas = sorted(lista,reverse=True,key=lambda p: p.sobrenome)
    print(ordenadas)
'''
269. asdict e astuple em dataclasses
'''
from dataclasses import asdict, astuple, dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

if __name__ == '__main__':
    p1= Pessoa('Luiz','Otávio')
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])

