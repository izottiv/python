nome = []
idade = []
for i in range(4):
    n = input()
    id = int(input())
    nome.append(n)
    idade.append(id)
ai = 0
idd = 0
for i in range(4):
    if idade[i] > ai:
        ai = idade[i]
        idd = i
print(ai, nome[idd])
