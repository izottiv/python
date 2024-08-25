n = 1
d = 1
nn = []
dd = []
f = []
for i in range(0, 51):
    f.append(n/d**3)
    print('{}/{}³'.format(n, d))
    d += 2
posi = []
negat = []
for j in range(len(f)):
    if j % 2 == 0:
        posi.append(f[j])
    else:
        negat.append(f[j])
for f in range(len(negat)):
    negat[f] = -negat[f]
negativ = sum(negat)
positiv = sum(posi)
print(negativ+positiv)
