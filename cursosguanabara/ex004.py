n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanúmerico? {}'.format(n.isalnum()))
print('Esta em maiúsculas? {}'.format(n.isupper()))
print('Esta em minúsculas? {}'.format(n.islower()))
print('Esta capitalizada? {}'.format(n.istitle()))
