'''
111. (Parte 1) *args para quantidade de argumentos não nomeados variáveis
'''
# x,y, *resto = 1,2,3,4
# print(x,y ,resto)
def soma(*args):
    total = 0 
    for numero in args:
        total = 0 
        for numero in args:
            total += numero 
        return total 
soma1 = soma(1,2,3)
soma2 = soma(4,5,6)

numeros = 1,2,3,4,5,6,7
outra_soma = soma(*numeros)
print(outra_soma)
print(sum(numeros))

print(soma1,'  ',soma2)
