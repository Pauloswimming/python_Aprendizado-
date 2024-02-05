"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = int(input('digite um numero:'))

# if numero%2==0 :
#     print('esse numero é par')
# elif numero%2!=0:
#     print('esse numero é impar')
# else:
#     print('vc deve digitar numeros.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# passageiro = input('moço que horas são:')

# try:
#     horas = int(passageiro)
#     if horas >=0 and horas <=11:
#         print('bom dia passageiro.')
#     elif horas >=12 and horas <=17:
#         print('boa tarde passageiro')
#     elif horas >=18 and horas <=23:
#         print('boa noite')    
#     else:
#         print('não reconheço esse horario')
# except:
#     print('por gentileza,digite o numeros!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('digite seu nome:')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <=4:
        print('seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('seu nome é normal')
    else:
        print('seu nome é muito grande.')
else:
    print('vc deve digitar mas de uma letra.')