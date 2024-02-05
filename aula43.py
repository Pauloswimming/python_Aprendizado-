# senhas_salva = '123456'
# senha_digitada = '' 
# repetições = 0

# while senhas_salva != senha_digitada:
#     senha_digitada = input(f'sua senha ({repetições}x):')
#     repetições += 1
# print(repetições)
# print('aquele laço acima pode ter repetições infinitas.')    

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')