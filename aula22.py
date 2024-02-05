# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor
'''
or aceita qualque uma que esteja verdadeira 
and so aceita se tudo for verdadeiro 
'''

entrada = input('[E]ntrar ou [S]air:')
senha_digitada = input('senha:')
senha_cadastrada = '12345678'

if (entrada == 'E' or entrada == 'e') and senha_digitada==senha_cadastrada:
    print('vc entrou')

else:
    print('vc saiu')

