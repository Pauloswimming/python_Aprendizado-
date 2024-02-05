'''
245. Método especial __call__
Método especial __call__
callable é algo que pode ser executado com parênteses
Em classes normais, __call__ faz a instância de uma
classe "callable".

__call__ Method:

Este é um método especial em Python que permite que uma instância de uma classe seja chamada como uma função.
Aqui, ele recebe um argumento nome e imprime uma mensagem indicando que a pessoa com o nome
fornecido está chamando o número de telefone associado à instância.
Além disso, ele retorna o valor 2134.
'''
class CallMe:
    def __init__(self,phone):
        self.phone = phone
    
    def __call__(self,nome):
        print(nome,'esta chamando',self.phone)
        return 2134

call1 = CallMe('61 3375-7051')    
retorno = call1('Mãe')
print(retorno)

