t = 10
m = [[0 for i in range(t)]for i in range(t)]
for l in range(t):
    for k in range(t):
        m[l][k] = int(input())
for ln in m:
    print(ln)
print('Todos os elementos, exceto os elementos da diagonal principal:')
for l in range(t):
    for k in range(t):
        if l != k:
            print(m[l][k])
print('Somente os elementos abaixo da diagonal principal:')
for a in range(t):
    for b in range(t):
        if a > b:
            print(m[a][b])
print('A soma de cada linha da matriz:')
for c in range(t):
    soma = sum(m[c])
    print(f'Soma da linha {c + 1}: {soma}')
for k in range(t):
    prod = 1
    for j in range(t):
        prod *= m[j][k]
    print(f'Produto da coluna {k + 1}: {prod}')
