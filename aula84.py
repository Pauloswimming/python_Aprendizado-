'''
136. Introdução à List comprehension em Python
Introdução à List comprehension em Python
List comprehension é uma forma rápida para criar listas
a partir de iteráveis.
print(list(range(10)))
'''
lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero * numero  #pega o numero é multiplica com ele: 1*1 ,2*2,3*3
    for numero in range(10)
]
print(lista)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco':20,},
    {'nome': 'p2', 'preco':10,},
    {'nome': 'p3','preco':30,},
]
novos_produtos = [
    {**produto,'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos 
]
# print(*novos_produtos,sep='\n')


'''
Introdução à List comprehension em Python
List comprehension é uma forma rápida para criar listas
a partir de iteráveis.
print(list(range(10)))
138. Filtro de dados em list comprehension (filter)
'''
import pprint

def p(v):
    pprint.pprint(v,sort_dicts=False,width=40)  #sort_dicts server apenas pra ordernar e width seria quantidade de caractere que vc quer 
lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero*2
    for numero in range(10)
]

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto,'preco':produto['preco'] * 1.05}  #isso server pra desempacotar uma lista grande é mudar o valor 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
novos_produtos = [
    {**produto,'preco':produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] *1.05) > 10
]
p(novos_produtos)

