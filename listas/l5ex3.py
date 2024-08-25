v = []
for i in range(15):
    v.append(int(input()))
r = v[0]
g = v[0]
idmin = idmax = 0
for j in range(15):
    if v[j] > r:
        r = v[j]
        idmax = j
    if v[j] < g:
        g = v[j]
        idmin = j
print(f'O maior valor se encontra na posição {idmax} do vetor'
      f'\nO menor valor é {v[idmin]} e se encontra na posição {idmin} do vetor')
