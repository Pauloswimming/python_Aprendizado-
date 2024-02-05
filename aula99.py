'''
157. Introdução aos packages (pacotes) em Python
terminal:ls | grep aula99
'''
# from sys import path 
# import aula99_package.modulo
# from aula99_package import modulo 
# from aula99_package.modulo import *

# print(soma_do_modulo(1,3))
# print(aula99_package.modulo.soma_do_modulo(1,3))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# print(__name__)


# from aula99_package.modulo import fala_oi, soma_do_modulo

from aula99_package import falar_oi1

# print(soma_do_modulo(2, 3))
falar_oi1()