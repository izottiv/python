poten = 25
deno = 1
n = int(input())
posi = []
negat = []
for i in range(1, 26):
    if i % 2 == 0:
        negat.append((n**poten)/deno)
    else:
        posi.append((n**poten)/deno)
    print('{}/{}'.format(n**poten, deno))
    poten -= 1
    deno += 1
for f in range(len(negat)):
    negat[f] = -negat[f]
soma = sum(negat)+sum(posi)
print(soma)
