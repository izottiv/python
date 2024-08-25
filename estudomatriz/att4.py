n = str(input())
t = 12
m = [[0 for i in range(t)]for i in range(t)]
for i in range(t):
    for j in range(t):
        m[i][j] = float(input())
som = c = 0
for i in range(t):
    for j in range(t):
        if i > j and (t-1-i) < j:
            if n == 's' or n == 'S':
                som += m[i][j]
            elif n == 'm' or n == 'M':
                som += m[i][j]
                c += 1
if n == 's' or n == 'S':
    print(f'{som:.1f}')
elif n == 'm' or n == 'M':
    print(f'{som/c:.1f}')
