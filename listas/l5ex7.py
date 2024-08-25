v = [i for i in range(50)]
aux = 49
for j in range(25):
    v[j], v[aux] = v[aux], v[j]
    aux -= 1
print(v)
