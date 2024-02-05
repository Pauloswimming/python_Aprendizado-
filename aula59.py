'''
96. Desempacotamento em chamadas de funções
'''
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]
print(*salas,sep='\n') #isso serve pra ver a lista 