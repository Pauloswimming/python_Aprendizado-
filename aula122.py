'''
201. Entendendo self em classes Python
# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
'''
class Carro:
    def __init__(self,nome):
        self.nome = nome
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar()
print()
Carro.acelerar(fusca)

print()

celta = Carro('Celta')
celta.acelerar()
print()
Carro.acelerar(celta)