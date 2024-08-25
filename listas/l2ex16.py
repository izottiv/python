n = int(input())
if n % 3 == 0 and n % 7 == 0:
    print('É divisivel por 3 e 7')
elif n % 3 == 0 and n % 7 != 0:
    print('É divisivel por 3')
elif n % 3 != 0 and n % 7 == 0:
    print('É divisivel por 7')
elif n % 3 != 0 and n % 7 != 0:
    print('Não é divisivel nem por 3 nem por 7')
