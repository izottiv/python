numeros = []
t = 100
for i in range(t):
    n = int(input())
    numeros.append(n)
for j in range(t-1):
    for j in range(t-1):
        if numeros[j] > numeros[j+1]:
            c = numeros[j+1]
            numeros[j+1] = numeros[j]
            numeros[j] = c
print(numeros)
