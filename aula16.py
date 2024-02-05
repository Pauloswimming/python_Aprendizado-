#33. Introdução aos blocos de código + if / elif / else (condicionais)

'''
if -- se
elif -- se não se
else -- se não 
'''

entrada = input('Digite pra entrar ou sair do sitema:')

if entrada == "entrar":
    print('vc entrou no sitema!')
elif entrada == "sair":
    print("vc saiu do sistema")
else:
    print("vc tem que digitar entrar ou sair no sistema")