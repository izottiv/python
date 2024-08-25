m = [[0 for i in range(5)]for i in range(10)]
for i in range(10):
    for j in range(5):
        m[i][j] = float(input())
r = 0
for l in range(10):
    som = sum(m[l])
    if som > r:
        r = som
        idd = l
print(m[idd], f'posição {idd+1}')
