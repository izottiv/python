from random import randint
TEMPERATURAS = [randint(15, 40) for i in range(121)]
som = 0
c1 = c2 = c3 = 0
for j in range(121):
    som += TEMPERATURAS[j]
media = som/121
for k in range(121):
    if TEMPERATURAS[k] < media:
        c1 += 1
for k in range(121):
    if TEMPERATURAS[k] < 20:
        c2 += 1
for k in range(121):
    if TEMPERATURAS[k] > 20:
        c3 += 1
print(f'Temperatura Média = {media:.1f}')
print(
    f'O número de dias nos quais a temperatura foi inferior à temperatura média = {c1}')
print(f'O número de dias que fez menos de 20 ºC = {c2}')
print(f'O número de dias que fez mais de 35 ºC = {c3}')
