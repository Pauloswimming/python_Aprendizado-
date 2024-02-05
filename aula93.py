'''
149. (Parte 1) try e except para tratar exceções

'''
try:
    a = 18
    b = 0 
    # print('linha 1'[1000])
    c = a / b 
    print('linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('dividiu por zero.')
except NameError:
    print('nome b não está definido')
except (TypeError,IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:',error)
    print('nome:',error.__class__.__name__)
except Exception:
    print('Errro desconhecido')
print('continuar')
