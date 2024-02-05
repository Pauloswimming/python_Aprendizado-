'''
Reproduzir
200. Métodos em instâncias de classes Python
resumir na propria aula 
'''
class Carro:
    def __init__(self,nome):
        self.nome = nome
    def acelerar(self):
        print(f'{self.nome} está acelerando...')
string = 'paulo'
print(string.upper())

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()