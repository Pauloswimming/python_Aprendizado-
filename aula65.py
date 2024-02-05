
'''
65 até 75
105. Introdução às funções Python - def define uma função
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
Funções podem usar parâmetros para receber valores.
Parâmetro é o nome da "variável" dentro dos parênteses,
argumento é o valor passado para o parâmetro no momento da execução da função.
'''


# def imprimir(a,b,c):  #isso seri Um parametro 
#     print(a,b,c)
# imprimir(1,2,3) #já isso seria um argumento pois tem valor 

# def saudacao(nome='Sem nome'):
#     print(f'olá,{nome}!')
# saudacao('luiz otario')
# saudacao('paulo')


def par_ou_impar(numero,m):
    if numero % m == 0:
        print(f'o numero é par')
    else:
        print('esse numero é impar')

par_ou_impar(9,2)


    


