'''
135. Empacotamento e desempacotamento de dicionários + *args e **kwargs
values seria pra entregar o valor da chave 
'''
a,b = 1,2
a,b = b,a 

pessoa = {
    'nome': 'aline',
    'sobrenome': 'sousa',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
pessoas_completa = {**pessoa,**dados_pessoa}#isso serve pra juntar os dicionarios é o desempacotamento


def mostro_argumentos_nomeados(*args,**kwargs):
    print('não nomeados:',args)
    for chave,valor in kwargs.items():
        print(chave,valor)
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,

}
mostro_argumentos_nomeados(**configuracoes)


