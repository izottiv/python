f = []
mm1 = []
mm2 = []
denn = []
m1 = 1
m2 = 2
den = 37
for i in range(1, 38):
    mm1.append(m1)
    mm2.append(m2)
    denn.append(den)
    f.append(m1 * m2/den)
    m1 += 1
    m2 += 1
    den -= 1
mm1.reverse()
mm2.reverse()
denn.reverse()
for j in range(len(mm2)):
    print('{} x {}/{}'.format(mm1[j], mm2[j], denn[j]))
print(sum(f))
