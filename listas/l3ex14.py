c1 = c2 = c3 = c4 = nu = br = rl = 0
while True:
    n = int(input())
    rl += 1
    if n == 1:
        c1 += 1
    elif n == 2:
        c2 += 1
    elif n == 3:
        c3 += 1
    elif n == 4:
        c4 += 1
    elif n == 5:
        nu += 1
    elif n == 6:
        br += 1
    print('votos 1° candidato =', f'{c1}'
          '\nvotos 2° candidato =', f'{c2}'
          '\nvotos 3° candidato =', f'{c3}'
          '\nvotos 4° candidato =', f'{c4}'
          '\nvotos nulos =', f'{nu}'
          '\nvotos em branco =', f'{br}'
          '\n% votos em branco ou nulos = {}%'.format(((nu+br)/rl)*100)

          )
