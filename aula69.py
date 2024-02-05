'''
109. (Parte 2) Escopo de funções e módulos em Python + global
'''
x = 1 
def escopo():
    global x 
    x = 10 
    def outra_funcao():
        global x 
        x = 11 
        y = 2
        print(x,y)
    outra_funcao()
    print(x)
print(x)
escopo()
print(x)