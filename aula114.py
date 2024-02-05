'''
# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
179. Funções recursivas, recursividade e Stack Overflow
180. Limite de recursão e cuidados com funções recursivas
'''

# import sys 
# sys.setrecursionlimit(1005)

# def recursiva(inicio=0,fim=4):
#     print(inicio,fim)
#     if inicio >= fim:
#         return fim
#     inicio +=1
#     return recursiva(inicio,fim)
# print(recursiva(0,1000))



def factorial(n): #isso serve pra fatorar o numero!
    if n <= 1:
        return 1 
    return n * factorial(n-1)
print(factorial(5))
print(factorial(10))
print(factorial(100))