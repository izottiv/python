po = []
som = 0
for i in range(6):
    n = float(input())
    if n > 0:
        po.append(n)
        som += 1
print('{} valores positivos'.format(len(po)))
print('{}'.format(sum(po)/som))
