from random import randint
v = [randint(1, 10) for i in range(100)]
n = int(input())
c = 0
for i in range(100):
    if n == v[i]:
        c = 1
if c == 1:
    print('O valor digitado existe no vetor')
else:
    print('O valor digitado não existe no vetor')
