v = [i for i in range(100)]
a = 99
b = 0
for i in range(50):
    v[b], v[a] = v[a], v[b]
    a -= 1
    b += 1
print(v)
