d = int(input())
if d >= 365:
    print('{} anos'.format(d/365))
else:
    print('0 anos')
if d >= 30:
    print('{} meses'.format(d/30))
else:
    print('0 meses')
print('{} dias'.format(d))
