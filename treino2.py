# prova1A.py
def geraValor1(entrada):
    return int(entrada[-3:])

# prova1B.py
def geraValor2(entrada):
    f = len(entrada) - 2
    return int(entrada[:f:2])

# prova1C.py
def processaValor1(entrada):
    nova_entrada = []
    i = 0
    seq = ''
    while i < len(entrada):
        if entrada[i] != '0':
            seq += entrada[i]
        else:
            if seq != '':
                nova_entrada.append(seq)
                seq = ''
        i += 1
    if seq != '':
        nova_entrada.append(seq)
    return nova_entrada

# prova1D.py
def processaValor2(entrada, filtro):
    var1 = []
    for item in entrada:
        if filtro not in item:
            var1.append(item)
    return var1

# prova1E.py
def geraValor3(entrada):
    ops = processaValor1(entrada)
    ref = None
    index = 0
    while index < len(ops):
        item = ops[index]
        item = int(item)
        if ref is None:
            ref = item
        else:
            if item > ref:
                ref = item
        index += 1
    return ref

# prova1F.py
def processaValor4(entrada):
    saida = ''
    for ix in range(len(entrada) - 1, -1, -1):
        saida += entrada[ix]
    return saida

# prova1G.py
def processaValor5(entrada, ref):
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for item in entrada:
        l[int(item)] += 1
    return l[ref]

# prova1H.py
def processaValor6(entrada):
    entrada = list(entrada)
    for i in range(1, len(entrada), 2):
        entrada[i - 1], entrada[i] = entrada[i], entrada[i - 1]
    return ''.join(entrada)

matricula = input()
print(geraValor1(matricula),'geravalor1')

matricula = input()
print(geraValor2(matricula),'gerar valor 2')

matricula = input()
print(processaValor1(matricula),'processar valor 1')

matricula = input()
print(processaValor2(matricula, '1'),'processar valor 2')

matricula = input()
print(geraValor3(matricula),'gerar valor 3')

matricula = input()
print(processaValor4(matricula),'gerar valor 4')

matricula = input()
print(processaValor5(matricula, 2),'gerar valor 5')

matricula = input()
print(processaValor6(matricula),'gerar valor 6')
