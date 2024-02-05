import os
'''
186. Criando arquivos com Python + Context Manager with
188. Modos de abertura de arquivo e encoding com with open
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')
'''
# caminho_aquivo = 'c:\\Users\\VAIO\\Desktop\\cursopython_novo\\venv\\Scripts\\Activate.ps1'
# caminho_aquivo += 'aula116.txt'

# caminho_aquivo = 'c:/Users/VAIO/Desktop/cursopython_novo/venv/Scripts/Activate.ps1'
# caminho_aquivo = 'aula116.txt'

# with open(caminho_aquivo,'w') as arquivo:
#     print('ola mundo')
#     print('arquivo vai ser fechado')

# with open(caminho_aquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())


# print('#' * 10)

# with open(caminho_aquivo, 'r') as arquivo:
#     print(arquivo.read())

'''
acentuação foi windos 1252 no UTF-8
'''
caminho_aquivo = 'aula116.txt'
with open(caminho_aquivo, 'w+',encoding='utf-8') as arquivo: #usa no windos pra aperecer a acentuação 
    arquivo.write('atenção 1\n')
    arquivo.write('cão doido 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.remove(caminho_arquivo) # ou unlink
os.rename(caminho_aquivo, 'aula116.txt')
