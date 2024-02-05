'''
while/else
'''
string = 'valor da variavel'
i = 0 
while i < len(string):
    letra = string[i]
    if letra == ' ':
        break
    i +=1
    print(letra)
else:
    print('não encontrei um espaço na string')
print('fora do bloco')