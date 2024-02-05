'''
Higher Order Functions
Funções de primeira classe
114. Higher Order Functions - Funções de primeira classes

'''
def saudacao(msg,nome):
    return f'{msg},{nome}'

def executa(funcao,*args):
    return funcao(*args)
print(
    executa(saudacao,'bom dia','luiz')

)
print(
    executa(saudacao,'boa noite','maria')
)