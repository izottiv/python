pares = []
impares = []
for i in range(1, 201):
    n = int(input())
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('Pares', len(pares))
print('Impares', len(impares))
