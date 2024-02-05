'''
144. dir, hasattr e getattr em Python
desbugador depois vai no debug console é coloque dir(str) pra saber quais metodos têm
vc deve fazer junto desbugando
'''
string = 'paulo'
metodo = 'strip'

if hasattr(string,metodo):
    print('existe upper')
    print(getattr(string,metodo)())
else:
    print('não existe o método',metodo)
