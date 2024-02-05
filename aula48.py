'''
bora fazer o seguinte 10 aulas por dia!
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''

# string = 'ABCDE'
#     #     0   1         2           3   4 
#     #    -5  -4        -3          -2  -1
# lista = [123,True,'Paulo Henrique',1.2,[]]
# lista[-3] = 'Maria'
# print(lista[2],type(lista[2]))
# print(lista)

# lista = [10,20,30,40]
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista,'removido',ultimo_valor)

# lista =[10,20,30,40]
# lista.append('Luiz')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# #lista.clear()
# lista.insert(100,5)
# print(lista[4])

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

# lista_a = ['luiz','maria',1,True,1.2]
# lista_b = lista_a.copy()

# lista_a[0] = 'Paulo H'
# print(lista_a)
# print(lista_b)