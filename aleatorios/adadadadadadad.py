matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
# Adição de matrizes
soma = []
for i in range(len(matriz1)):
    linha = []
    for j in range(len(matriz1[0])):
        linha.append(matriz1[i][j] + matriz2[i][j])
    soma.append(linha)
for linha in soma:
    print(linha)
