contas = []
agencias = []
saldos = []
aux = []
c = n = 0
t = 3
for i in range(t):
    contas.append(int(input()))
    agencias.append(input())
    saldos.append(float(input()))
for j in range(t):
    print("Conta = {}".format(contas[j]))
    print("Agência = {}".format(agencias[j]))
    print("Saldo = {}".format(saldos[j]))
    if saldos[j] > 0:
        print("positivo")
    else:
        print("negativo")
for l in range(t):
    if agencias[l] not in aux:
        aux.append(agencias[l])
        n = c = 0
        for k in range(t):
            if agencias[l] == agencias[k]:
                c += 1
                if saldos[k] < 0:
                    n += 1
        print('A agência {} possui {} pessoas'.format(agencias[l], c))
        print("{}% estão negativados".format((n / c) * 100))
