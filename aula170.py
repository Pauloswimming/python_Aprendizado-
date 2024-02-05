'''
283. os.listdir para navegar em caminhos
# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:/Users/luizotavio/Desktop/EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
C:/Users/VAIO\3D Objects/imagens
'''
# import os 
# caminho = os.path.join('/Users','/VAIO','/3D Objects','/images')

# for pasta in os.listdir(caminho):
#     caminho_completo_pasta = os.path.join(caminho,pasta)
#     print(pasta)

#     if not os.path.isdir(caminho_completo_pasta):
#         continue

#     for imagem in os.listdir(caminho_completo_pasta):
#         print(' ',imagem)


import os
#esse dá certo

# Use barras inclinadas (/) ou barras invertidas (\) para especificar caminhos no Windows
caminho = os.path.join('C:/Users', 'VAIO', '3D Objects', 'imagens')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print(' ', imagem)
