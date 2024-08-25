d = int(input())
if d >= 365:
    ano = d/365
    print('{} anos'.format(ano))
if d == 0:
    print('0 anos')
    if d % 365 >= 30:
        meses = (d % 365)/30
        print('{} meses'.format(meses))
        if d % 30 > 0:
            dias = d
            print('{} dias'.format(dias))
        if d % 30 == 0:
            print('0 dias')
    if d % 365 == 0:
        print('0 meses')
if d >= 30 and d < 365:
    meses = d/30
    print('{} meses'.format(meses))
    if d % 30 > 0:
        dias = d
        print('{} dias'.format(dias))
    if d % 30 == 0:
        print('0 dias')
if d > 0 and d < 30:
    dias = d
    print('{} dias'.format(dias))
if d == 0:
    print('0 dias')
