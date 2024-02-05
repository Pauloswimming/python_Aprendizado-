'''
165. Funções decoradoras em geral
Funções decoradoras e decoradores
Decorar = Adicionar / Remover/ Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python
usar as funções decoradoras em outras funções.
'''
def criar_funcao(func):
    def interna(*args,**kwargs):
        print('vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args,**kwargs)
        print(f'o seu resultado foi {resultado}.')
        print('ok,agora vc foi decorada')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]
def e_string(param):
    if not isinstance(param,str):
        raise TypeError('param deve ser uma str')
inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)