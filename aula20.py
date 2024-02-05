#Solução - Exercício de programação com if e comparação
primeiro_valor = int(input('digite um valor inteiro:'))
segundo_valor = int(input('digite um valor inteiro:'))

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior que {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'{primeiro_valor} é menor que {segundo_valor}')
elif primeiro_valor==segundo_valor:
    print(f'{primeiro_valor} são iguais {segundo_valor}')
else:
    print('vc deve digitar um numero!')
