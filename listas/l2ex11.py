a = int(input())
b = int(input())
if b == 0:
    print('Não se pode dividir por 0')
else:
    if a % b == 0:
        print('É divisivel')
    else:
        print('Não é divisivel')
