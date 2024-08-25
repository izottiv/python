v = []
for i in range(30):
    v.append(int(input()))
for j in range(30):
    if j % 2 == 0:
        v[j] = 0
print(v)
