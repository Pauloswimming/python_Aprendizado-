'''
113. Exercícios com funções + Solução (prepare-se para pausar)
 Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.
'''
def multiplicar(*args):
    total = 1 
    for numero in args:
        total *= numero
    return total
multiplicação = multiplicar(10,2,3,4,5)
print(multiplicação)

def par_impar(numero):
    muliplo_de_dois = numero % 2 == 0
    if muliplo_de_dois:
        return f'{numero} é par'
    else:
        return f'{numero} é ímpar'

outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))



