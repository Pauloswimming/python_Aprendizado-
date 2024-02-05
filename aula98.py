'''
156. Recarregando módulos, importlib e singleton
amanha fazer revisão é assitir 10 aulas fazendo revisão 
'''
import importlib
import aula98_m
print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)
print('fim.')