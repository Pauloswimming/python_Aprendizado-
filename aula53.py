'''
enumerate - enumera iteráveis (índices)
'''
lista = ['maria','helena','luiz']
lista.append('joão')
for indice,nome in enumerate(lista):
    print(indice,nome,lista[indice])
    