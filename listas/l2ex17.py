n = int(input())
if n < 16:
    print('Não eleitor')
elif n >= 18 and n < 65:
    print('Eleitor obrigatório')
elif n >= 16 and n < 18 or n >= 65:
    print('Eleitor facultativo')
