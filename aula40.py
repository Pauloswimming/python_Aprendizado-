
#calculdadora exercicio
'''
lower é pra transformar tudo em minusculo
startswith serve pra transformar em booleano true or false 

'''

while True:
    numero_1 = input('digite um numero:')
    numero_2 = input('digite um numero:')
    operador = input('digite um desses operadores(*/+-):')
    numeros_validos = None 
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True 
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('um ou ambos estão errados.')
        continue
    operadores_permitido = '*/+-'
    if operador not in operadores_permitido:
        print('digite um operador.')
        continue
    if len(operador) > 1 :
        print('digite apenas um operador.')
        continue
    sair = input('quer sair?sim:').lower().startswith('s')

    if sair is True:
        break
    
    print('realizando a conta.Confira o valor abaixo.')

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} =', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = ',numero_1_float - numero_2_float)
    elif operador == '/':
         print(f'{numero_1_float} / {numero_2_float} = ',numero_1_float / numero_2_float)
    elif operador == '*':
         print(f'{numero_1_float} * {numero_2_float} = ',numero_1_float * numero_2_float)
    else:
        print('opa como assim vc não era pra parecer (-_-)')
    
    
    