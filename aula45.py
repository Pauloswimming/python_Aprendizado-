'''
aula sobre for como funciona,mas por curiosidade.
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''
# texto = 'Paulo'
# iteratador = iter(texto)
# while True:
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

texto = 'Paulo'
for letra in texto:
    print(letra)