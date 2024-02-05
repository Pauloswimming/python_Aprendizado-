'''
204. Atributos de classe
'''
class Pessoa:
    ano_atual = 2022
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('joão',43)
p2 = Pessoa ('cirene',99)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())