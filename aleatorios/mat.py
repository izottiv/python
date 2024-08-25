m = [[0 for i in range(3)]for i in range(3)]
for j in range(3):
    for k in range(3):
        m[j][k] = int(input())
tras = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(m[j][i])
    tras.append(linha)
for a in m:
    for b in a:
        print(b, end=' ')
    print()
print('-'*80)
for a in tras:
    for b in a:
        print(b, end=' ')
    print()
