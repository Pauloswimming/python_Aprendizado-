'''
130. Exemplo de uso do tipo set
'''
letras = set()
while True:
    letra = input('digite:')
    letras.add(letra.lower())
    if 'l' in letras:
        print('parabéns')
        break
    print(letras)