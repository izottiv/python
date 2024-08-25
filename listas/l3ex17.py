f = []
num = 1
den = 1
for i in range(1, 50):
    print('{}/{}'.format(num, den))
    num += 2
    den += 1
    f.append(num/den)
print(sum(f))
