#30. Uma introdução às f-strings (formatação de strings)

nome = 'Paulo Henrique'
altura = 1.72
massa = 65
imc = massa/altura**2

linha_1 = f'seu nome é {nome},com isso a sua altura é {altura}'
linha_2 = f'sabemos que sua massa é {massa},então seu imc é {imc:.2f},ou seja,seu peso esta normal'
print(linha_1)
print(linha_2)

