'''
270. Valores padrão, field e fields em dataclasses
# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
'''
from dataclasses import dataclass,field

@dataclass
class Pessoa:
    nome: str = field(
        default= 'MISSING',repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)

if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)