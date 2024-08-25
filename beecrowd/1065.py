par = []
for i in range(5):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
print('{} valor(es) par(es)'.format(len(par)))
