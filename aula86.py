'''
Dictionary Comprehension e Set Comprehension
141. Dictionary Comprehension e Set Comprehension
'''
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
} 

dc = {
    chave: valor.upper()
    if isinstance(valor,str) else valor 
    for chave, valor 
    in produto.items() #usa isso pra aparecer os valores pois tem mais um item 
    if chave != 'categoria'

}

lista = [
    ('a','valor a'),
    ('b','valor a'),
    ('b','valor a'),
]

dc = {
    chave: valor 
    for chave,valor in lista 
}
s1  = {2** i for i in range(10)}
print(s1)