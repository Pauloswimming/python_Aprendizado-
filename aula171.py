'''
284. os.walk para navegar de caminhos de forma recursiva
'''
import os
caminho = os.path.join('C:/Users', 'VAIO', '3D Objects', 'imagens')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho,pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue
    for imagem in os.listdir(caminho_completo_pasta):
        print(' ',imagem)

