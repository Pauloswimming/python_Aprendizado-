#39. Operador Lógico "and"
'''
and(e) or(ou) not(não)

and- todas condições tem que ser verdadeira se não tudo é falso
'''

entrada = input('[E]ntrar ou [S]air:')
senha_1 = input('digita a senha:')
senha_2 = '04082004'

if entrada == 'E'  and senha_1 == senha_2:
    print("vc entrou abestado ")
else:
    print('vc saiu')