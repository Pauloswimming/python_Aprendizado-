#27. Precedência entre os operadores aritméticos

'''
a ordem de operaçôes pra serem executadas:
primeiro (n+n)
segundo ** potenciação 
terceiro * / // %
quarto + - 
'''
conta_1 = 1 + 1**5 + 5  #7
print(conta_1)

conta_2 = (1+1)**(5+5) #1024
print(conta_2)

conta_3 = (1 + int(0.5+0.5)) ** (5+5) #outra forma!
print(conta_3)