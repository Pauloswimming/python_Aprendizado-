'''
181. O que são ambientes virtuais? (venv)
# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.

# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env
# Como criar ambientes virtuais
# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv  venv - isso server pra criar um ambiete virtual
python -V  indica versão do python!

# Abra a pasta do seu projeto no terminal
# e digite:
# python -m venv venv
#
# Ativando e desativando meu ambiente virtual
# Windows: .\venv\Scripts\activate
# Linux e Mac: source venv/bin/activate
# Desativar: deactivate

Parar
183. Ativando e desativando o meu ambiente virtual venv


# Linux e Mac: source venv/bin/activate
# Desativar: deactivate
#
# pip - instalando pacotes e bibliotecas
# Instalar última versão:
# pip install nome_pacote
# Instalar versão precisa
# (tem outras formas também não mencionadas)
# pip install nome_pacote==0.0.0
# Desinstalar pacote
# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze
184. pip - instalando pacotes e bibliotecas

185. Criando e usando um requirements.txt
# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze
#
# Criando e usando um requirements.txt
# pip freeze > requirements.txt
# Instalando tudo do requirements.txt
# pip install -r requirements.txt
'''
print('olá mundo caotico e perfeito')

