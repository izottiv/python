par = []
impar = []
posi = []
negat = []
for i in range(5):
    x = int(input())
    if x > 0:
        posi.append(x)
    if x < 0:
        negat.append(x)
    if x % 2 == 0:
        par.append(x)
    if x % 2 != 0:
        impar.append(x)
print('{} valor(es) par(es)'.format(len(par)))
print('{} valor(es) impar(es)'.format(len(impar)))
print('{} valor(es) positivo(s)'.format(len(posi)))
print('{} valor(es) negativo(s)'.format(len(negat)))
