n = int(input())
if n < 1 or n > 12:
    print('Mês inválido')
if n >= 1 and n <= 3:
    print('Primeiro trimestre')
if n >= 4 and n <= 6:
    print('Segundo trimestre')
if n >= 7 and n <= 9:
    print('Terceiro trimestre')
if n >= 10 and n <= 12:
    print('Quarto trimestre')
