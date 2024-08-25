lista = []
soma = 0
while True:
    n = int(input())
    if n == (-1):
        break
    soma = soma + n
    lista.append(n)
media = soma/len(lista)
print(media)
