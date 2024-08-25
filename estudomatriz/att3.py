"""3) Preencha uma matriz 5X15 com valores lidos pelo teclado.
Imprima na tela os elementos da primeira coluna e o somatório
da coluna da posição 5 da matriz"""
a = 5
b = 15
m = [[0 for i in range(b)]for j in range(a)]
for i in range(a):
    for j in range(b):
        m[i][j] = int(input())
for lin in m:
    print(lin)
for j in range(a):
    print(m[j][0])
print()
som = 0
for l in range(b):
    som += m[4][l]
print(som)
