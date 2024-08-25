divisor = int(input('divisor = '))
dividendo = int(input('dividendo = '))
if divisor == 0:
    print('Divisão não permitida')
else:
    print('quociente = {}'.format(dividendo/divisor))
    print('resto = {}'.format(dividendo % divisor))
