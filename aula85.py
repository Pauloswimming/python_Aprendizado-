'''
139. List comprehension com mais de um for
 https://youtu.be/1YbTDczvqco se quiser saber mais cobre isso!
'''
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x,letra) for letra in 'luiz']
    for x in range(3)
]
print(lista)
