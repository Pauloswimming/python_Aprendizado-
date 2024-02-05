'''
145. Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores)
146. Generator expression, Iterables e Iterators em Python
'''
# iterable = ['eu','tenho','_ter_']
# iterator = iter(iterable) #tem_iter_e_next_
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
import sys 

iterable = ['eu','tenho','_ter_']
iterator = iter(iterable) #tem_iter_e_next_  #entrega um valor por vez 
lista = [n for n in range(100000)]
generator = (n for n in range(100000))
print(sys.getsizeof(lista))  #isso serve pra não deixar a memoria pesada!
print(sys.getsizeof(generator)) 
print((generator))#se quiser chama list pra ver o código