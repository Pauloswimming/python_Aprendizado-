'''
92. Imprecisão dos números de ponto flutuante + round e decimal.Decimal
'''
import decimal
numero_1 = decimal.Decimal('0.01')
numero_2 = decimal.Decimal('0.07')
numero_3 = numero_1 + numero_2 
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3,3))