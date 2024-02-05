'''
Closure e funções que retornam outras funções
116. Closure e funções que retornam outras funções
ctrl+shift+p remove all breakingpont 
'''
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao},{nome}!'
    return saudar
falar_bom_dia = criar_saudacao('bom dia')
falar_boa_noite = criar_saudacao('boa noite')

for nome in ['maria','joana','luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
    