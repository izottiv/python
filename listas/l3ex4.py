lista = []
for i in range(100, 201):
    lista.append(i)
a = 100
b = 0
for j in range(50):
    lista[b], lista[a] = lista[a], lista[b]
    b += 1
    a -= 1
print(lista)
