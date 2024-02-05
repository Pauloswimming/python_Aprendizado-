'''
Formatação de strings com f-strings

'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.4873:0=10,.2f}')
print(f'{variavel: <10}')
print(f'o hexadecimal é de 1500 é {1500:08X}')
print(f'{variavel!r}')