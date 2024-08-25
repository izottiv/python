from random import randint
v1 = [randint(0, 999999) for i in range(75)]
v2 = [randint(0, 999999) for i in range(75)]
v3 = []
for i in range(75):
    v3.append(v1[i] + v2[i])
