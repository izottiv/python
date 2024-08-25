a = [i for i in range(10, 21)]
n = int(input())
li = []
inn = 0
for j in range(0, n):
    num = int(input())
    li.append(num)
for f in a:
    for k in li:
        if k == f:
            inn += 1
print('{} in'.format(inn))
print('{} out'.format(n - inn))
