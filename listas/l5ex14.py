m = [[0 for i in range(25)]for i in range(5)]
for j in range(5):
    for l in range(25):
        m[j][l] = int(input())
for i in range(5):
    print(m[i][0])
som = 0
for i in range(5):
    som += m[i][5]
print(som)
