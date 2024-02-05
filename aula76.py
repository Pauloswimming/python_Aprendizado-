'''
# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

'''
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
# }
# print(pessoa['nome'])
# print(pessoa['sobrenome'])
# print()
# for chave in pessoa:
#     print(chave,pessoa[chave])

# print(pessoa, type(pessoa))


# Manipulando chaves e valores em dicionários
#120. Manipulando chaves e valores em dicionários em Python
# pessoa = {}
# chave = 'nome'
# pessoa[chave] = 'luiz otávio'
# pessoa['sobrenome'] = 'miranda'
# print(pessoa[chave])
# pessoa[chave] = 'maria'
# # del pessoa['sobrenome'] #isso muda o código no if e else
# print(pessoa)
# print(pessoa['nome'])
# # print(pessoa.get('sobrenome'))
# if pessoa.get('sobrenome') is None:    
#     print('NÃO EXISTE')
# else:
#     print(pessoa['sobrenome'])
#print('isso não vai)



'''
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
121. (Parte 1) Métodos úteis nos dicionários Python (dict)
'''
# pessoa = {
#     'nome': 'Paulo',
#     'sobrenome': 'miranda',
#     'idade': 900,
# }
# pessoa.setdefault('idade',0)
# print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)
# for chave, valor in pessoa.items():
#     print(chave,valor)

# import copy 
# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2],
# }
# d2 = d1.copy()
# d2['c1'] = 1000
# d2['l1'][1] = 99999

# print(d1)
# print(d2)


p1 = {
    'nome' : 'luiz',
    'sobrenome' : 'miranda' ,

}
lista = [['nome','novo valor'],['idade',30]]
p1.update(lista)
print(p1)
