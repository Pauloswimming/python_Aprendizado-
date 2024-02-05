'''
191. Problema dos parâmetros mutáveis em funções Python
# Problema dos parâmetros mutáveis em funções Python
# dica de programação tentar explicar o código pra vc mesmo!como se tivesse explicando pra outra pessoa!
'''
def adiciona_clientes(nome,lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista 

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('joana',cliente1)
adiciona_clientes('fernando',cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('helena')
adiciona_clientes('maria',cliente2)

cliente3 = adiciona_clientes('moreira')
adiciona_clientes('benjamin',cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
