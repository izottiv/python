km = float(input('Quantos Km rodados? '))
d = int(input('Quantos dias alugados? '))
preço = (60*d) + (0.15*km)
print('O preço a pagar é de R$ {:.2f}'.format(preço))
