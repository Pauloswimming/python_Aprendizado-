'''
142. isinstace() - para saber se objeto é de determinado tipo
# isinstace - para saber se objeto é de determinado tipo
'''
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]
for item in lista:
    if isinstance(item,set):
        print('SET') #set de conjuntos 
        item.add(5)
        print(item,isinstance(item,set))
    elif isinstance(item,str):
        print('STR')  #strings 
        print(item.upper())
    elif isinstance(item,(int,float)):
        print('NUM')  #numero 
        print(item,item*2)
    else:
        print('OUTRO')  
        print(item)