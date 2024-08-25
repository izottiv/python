x = 1
y = 1
n = [x, y]
for i in range(1, 19):
    t = y+x
    x = y
    y = t
    n.append(t)
print(n)
