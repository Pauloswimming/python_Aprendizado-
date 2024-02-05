'''
49. Parte 1: Variáveis, constantes e complexidade de código

CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

'''

# velocidade = 80  # velocidade atual do carro
# local_carro = 100  # local em que o carro está na estrada

# RADAR_1 = 60
# LOCAL_1 = 100
# RADAR_RANGE = 1

# velocidade_carro_passar_radar_1= velocidade > RADAR_1
# carro_passou_radar_1= local_carro >= (LOCAL_1 + RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
# carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passar_radar_1

# if velocidade_carro_passar_radar_1:
#     print('velocidade carro passou do radar 1')
# if carro_passou_radar_1:
#     print('carro passou radar 1')
# if carro_multado_radar_1:
#     print('carro multado em radar 1')

velocidade = 60  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada
RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')

'''
recado vc vai revisar as 10 ultimas aulas,depois continuar.
olhar o que eu errei nesse codigo 
'''
 
