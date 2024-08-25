""""1) Crie um algoritmo que leia valores do teclado e preencha uma matriz 5x5 na
ordem de uma linha de cada vez. Imprima os valores.
"""
m = [[0 for i in range(5)]for i in range(5)]
for i in range(5):
    for j in range(5):
        m[i][j] = int(input())
for linha in m:
    print(linha)
