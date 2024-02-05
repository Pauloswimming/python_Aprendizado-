'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
pra acabar com loop aperte ctrl + c
'''

# condicao = True  cuidado loop infinito!

# while condicao:
#     print(1)
#     print(2)
#     print(3)

condicao = True

while condicao:
    nome = input('digite seu nome:')
    print(f'seu nome é {nome}')
    if nome == 'sair':
        break
print('acabou porra.')
