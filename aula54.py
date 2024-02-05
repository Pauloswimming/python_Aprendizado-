'''
91. Solução do exercício - crie uma lista de compras com listas (com try / except)
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
ctrl + . 
'''
import os
lista = []
while True:
    print('selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar:')
    if opcao == 'i':
        os.system('cls')
        Valor = input('valor:')
        lista.append(Valor)
    elif opcao == 'a':
        indice_str = input('escolha o índice para apagar:')
        try:
            indicie = int(indice_str)
            del lista[indicie]
        except ValueError:
            print('por favor digite número int.')
        except IndexError:
            print('índice não existe na lista ')
        except Exception:
            print('erro desconhecido')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('nada a listar')
        for i,Valor in enumerate(lista):
            print(i,Valor)
    else:
        print('por favor,escolha i,a ou l.')
