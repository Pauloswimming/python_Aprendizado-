'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar.
'''

# numero = input('qualquer numero que vc digitar vou dobrar:')
# numero_float = float(numero)
# print(f'o dobro do numero {numero} é {numero_float*2:.0f}')

numero_str = input('qualquer numero que vc digitar vou dobrar:')

try:
    numero_float = float(numero_str)
    print('float:',numero_float)
    print(f'o dobro do numero {numero_str} é {numero_float*2}')
except:
    print('Isso não é um numero.')

