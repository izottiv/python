from math import sqrt
n = int(input())
if n >= 0:
    print('A raiz quadrada do número é {}'.format(sqrt(n)))
else:
    print('O quadrado do número é {}'.format(n**2))
