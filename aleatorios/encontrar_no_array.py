f = [1, 2, 3, 4, 5, 'roberto', 13, 13]
idd = 0
for i in f:
    if i == 'roberto':
        break
    else:
        idd += 1
print(f[idd], idd)
