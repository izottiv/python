from random import randint
v = [randint(1, 100) for i in range(1000)]
n = int(input())
c = 0
for i in range(1000):
    if n == v[i]:
        c += 1
print(f'Esse valor se repete {c} vezes')
