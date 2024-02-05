'''
106-110

106. Argumentos nomeados e argumentos posicionais (não nomeados) em funções
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''
def soma(x,y,z):
    #definição 
    print(f'{x=} {y=} {z=}','|','x+y+z=',x  + y + z)   #x= seria os nomeados 

soma(1,2,3)
soma(1,y=2,z=5)
print(1,2,3,sep="-")
