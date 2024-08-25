v = []
for i in range(20):
    v.append(int(input()))
r = v[0]
idmin = idmax = 0
for j in range(20):
    if v[j] > r:
        r = v[j]
        idmax = j
    if v[j] < v[0]:
        r = v[j]
        idmin = j
print(f'maior valor = {v[idmax]}\nmenor valor = {v[idmin]}')
