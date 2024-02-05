# print("hello world,it's me paulo") #isso é um comentario abestado 
'''
isso é um docstring
'''
# print(12,34,sep=',',end='##\n##')
# print('\n')
# print('oi')

# print('Paulo','Henrique',sep=' ')
# print(type(int('b')))

# nome = input('what is your name?')
# idade = int(input('how old are you?'))
# maior_idade = idade >= 18

# print(f'my name is {nome},am i bigger? {maior_idade}')

# subtração = 10 - 9 
# print(subtração)

# adição = 20 + 23
# print(adição)

# multiplicação = 20 * 23 
# print(multiplicação)

# divisão = 10//5.5 #a diferença da divisão de \ ou \\ que uma dá decimal e outra arendonda 
# print(divisão)

# pontenciação = 20**2
# print(pontenciação)


# resto_de_divisão_ou_modulo = 10%3
# print(resto_de_divisão_ou_modulo) # se seu 0 é par se não é impar

# concatenação = 'paulo' + '123'*5
# print(concatenação)

# print((5+5)*2)
# print(5+5*2)


# nome = input('digite seu nome:')
# idade = int(input('quantos anos vc tem?'))
# massa = int(input('quanto de massa vc tem?'))
# altura = float(input('qual é sua altura?'))
# imc = massa/(altura**2)


# print(f'meu nome é {nome} , tenho {idade} anos minha massa e altura são {massa}, {altura} e meu imc seria {imc:.2f}')

# a = 'aaa'
# b = 'bbb'
# c = 'ccc'

# string = 'a = {},b = {},c = {} '
# formatação = string.format(a,b,c)
# print(string)

# senha = input('digite a sua senha:')
# senha_1 = '12345678'

# if senha_1 == senha:
#     print('vc entrou no sistema')
# else:
#     print('vc não entrou no sistema')


# entrar = input('digite entrar ou sair do sistema:')

# if entrar == 'entrar' or entrar == 'e' or entrar == 'E':
#     print('vc entrou no sistema')

# elif entrar == 'sair' or entrar == 's' or entrar == 's':
#     print('vc saiu do sitema')

# else:
#     print('vc deve digitar sair ou entrar')

# comparação = int(input('digite um numero:'))
# comparação_2 = int(input('digite um numero:'))

# if comparação > comparação_2:
#     print(f'o primeiro numero {comparação} é maior que segundo numero {comparação_2}')

# elif comparação < comparação_2:
#     print(f'o primeiro numero {comparação} é menor que segundo numero {comparação_2}')

# elif comparação == comparação_2:
#     print(f'o primeiro numero {comparação} é igual ao segundo numero {comparação_2}')

# else:
#     print('escreva apenas numeros!')

# nome = input('digite seu nome:')
# encontrar = input('o que tem  no seu nome:')

# if encontrar in nome:
#     print(f' no nome {nome} tem essas letras {encontrar}')

# elif encontrar not in nome:
#     print(f' no nome {nome} não tem essas letras {encontrar}')

# produto = 'danone de sabor ouro'
# preço = 1000000

# valor = 'o produto %s, tem o preço %.2f' %(produto,preço)
# print(valor)

# variavel = 'mundo'
# print(len(variavel)) #len ler qtd de caracteres 
# print(variavel[4:6])
# print(variavel[::-1])

'''
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios.
'''

# nome = input('digite seu nome:')
# idade = input('digite a sua idade:')

# if nome:
#     print(nome)
#     if nome:
#         print(nome[::-1])
#         if ' ' in nome:
#             print('seu nome possui espaços')
# print(len(nome),' letras ')
# print(nome[0])
# print(nome[-1])
# numero_str = input('digite qualque numero é vou dobrar: ')
# try:
#     numero_float = float(numero_str)
#     print('float;',numero_float)
#     print(f'o numero é {numero_str} é seu dobro é {numero_float*2}')
# except:
#     print('vc deve digitar numeros')

#parou na 30 

# velocidade = float(input('Digite a sua velocidade:')) #velocidade atual do carro
# local_carro = float(input('Digite a sua distancia do radar:')) #local do carro
# RADAR_1 = 60 #velocidade do radar em que pega 
# LOCAL_RADAR = 100  #distancia do radar
# RADAR_RANGE = 1  #onde o radar pega na distancia 

# multa = velocidade > RADAR_1
# distancia = local_carro >= (LOCAL_RADAR - RADAR_RANGE) and \
#     local_carro <= (LOCAL_RADAR - RADAR_RANGE)
# multa_efetivada = distancia and multa 
# não_teve_multa = velocidade < RADAR_1

# if multa_efetivada or multa:
#     print(f'sua velocidade foi {velocidade} km\h é ultrapassou a velocidade maxima do radar que é {RADAR_1}')

# elif não_teve_multa:
#     print(f'sua velocidade foi {velocidade} km\h permitida pela via ')
# else:
#     print('digite numeros!')

'''Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.'''

# horario = int(input('digite o horario pra se comprimentado da maneira certa:'))

# if horario >= 0 and horario <= 11:
#     print(f'bom dia,são {horario} horas')

# elif horario >= 12 and horario <= 17:
#     print(f'boa tarde,são {horario} horas')

# elif horario >= 18 and horario <=23:
#     print(f'boa noite,são {horario} horas')
# else:
#     print('por favor digite o horario certo!')

'''Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". '''

# nome = input('digite apenas o seu primeiro nome:')
# lendo_nome = len(nome)

# if lendo_nome > 1:
#     if lendo_nome <=4:
#         print('seu nome é curto')
#     elif lendo_nome <= 6:
#         print('seu nome é normal')
#     elif lendo_nome > 6:
#         print('seu nome é muito grande')
# else:
#     print('digite mais de uma letra')

# nome = 'paulo henrique'
# outra_variavel = f'{nome[:4]}ão {nome[5:14]}'

# print(nome)
# print()
# print(outra_variavel)

# condição = True 
# while condição:
#     nome = input('digite seu nome:')
#     if nome == 'sair':
#         print('acabou')
#         break

# qtd_colunas = 5
# qtd_linhas = 5 
# linha = 1 
# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna +=1
#     linha +=1
# print('acabou')
    
#40 parou

while True:
    numero_1 = input('digite um numero: ')
    numero_2 = input('digite outro numero: ')
    operador = input('digite uns desses operadores: ')
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
        print('um ou ambos estão incorretos!')
        continue
    operadores_permitido = '*\+-**'
    if operador not in operadores_permitido:
        print('digite um operador!')
    sair = input('que sair?sim? ').lower().startswith('s')

    if sair is True:
        break
    print('realizando a conta confira o valor abaixo')

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} = {numero_1_float + numero_2_float}')

    if operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = {numero_1_float - numero_2_float}')
    
    if operador == '*':
        print(f'{numero_1_float} * {numero_2_float} = {numero_1_float * numero_2_float}')
    if operador == '/':
        print(f'{numero_1_float} / {numero_2_float} = {numero_1_float / numero_2_float}')
    if operador == '**':
        print(f'{numero_1_float} ** {numero_2_float} = {numero_1_float ** numero_2_float}')
    else:
        print('como assim isso não era pra parecer (-..-)')
#parou na 40
'''
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0 
flutuante = 0.0 
nada = None 
falso = False
intervalo = range(0)'''

        
        