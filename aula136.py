'''
217. Composição - Python Orientado a Objetos
# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
'''

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self,rua,numero):
        self.enderecos.append(Endereco(rua,numero))
    
    def inserir_endereco_externo(self,endereco):
        self.enderecos.append(endereco)
    
    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua,endereco.numero)
    
    def __del__(self):
        print('Apagando',self.nome)

class Endereco:
    def __init__(self,rua,numero):
        self.rua = rua 
        self.numero = numero 
    def __del__(self):
        print('Apagando',self.rua,self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('av brasil',54)
cliente1.inserir_endereco('rua b',60)
endereco_externo = Endereco('av saudade',123)
cliente1.inserir_endereco_externo(endereco_externo) 
cliente1.listar_endereco()

del cliente1

print(endereco_externo.rua,endereco_externo.numero)
print('#### AQUI TERMINA MEU CÓDIGO')
    
        