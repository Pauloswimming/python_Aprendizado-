'''
42-Operadores in e not in
as strings são interaveis:
 0 1 2 3 4  
 P A U L O    
-5-4-3-2-1
not in --- não esta 
in ---- está 
'''

'''nome = 'Paulo'

print('ulo' in nome )
print('lolota' in nome)
print(10*'-')
print('ulo'not in nome)
print('lolota'not in nome )'''


nome = input('digite seu nome:')
encontrar = input('digite o que tem no nome:')

if encontrar in nome:
    print(f'{encontrar} esta no {nome}')
else:
    print(f'{encontrar} não esta no {nome}')
