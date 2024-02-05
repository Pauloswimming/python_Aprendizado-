'''
198. class - Classes são moldes para criar novos objetos 
toda aula vai comentar cada codigo!
# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
'''

# class Pessoa:
#     ...
# p1 = Pessoa()
# p1.nome = 'Paulo'
# p1.sobrenome = 'Nogueira'
# print()
# p2 = Pessoa()
# p2.nome = 'Paulo'
# p2.sobrenome = 'César'

# print(p1.nome)
# print(p1.sobrenome)
# print()
# print(p2.nome)
# print(p2.sobrenome)


'''
199. Introdução ao método __init__ (inicializador de atributos)
'''

class Pessoa:
    def __init__(self,nome,sobrenome): 
        self.nome = nome
        self.sobrenome = sobrenome 
p1 = Pessoa('paulo','nogueira')
# p1.nome = 'Paulo'
# p1.sobrenome = 'Nogueira'
print()
p2 = Pessoa('paulo','césar')
# p2.nome = 'Paulo'
# p2.sobrenome = 'César'

print(p1.nome)
print(p1.sobrenome)
print()
print(p2.nome)
print(p2.sobrenome)

#selfa == p1 isso serve pra facilitar vc não ter que criar mais codigos,vc ja passa dentro do objeto!
