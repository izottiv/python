"""2) Considere uma matriz de valores de notas de atletas numa olimpíadas em que cada
linha representa um atleta e cada coluna a nota de um jurado. Considerando uma
matriz de 10 atletas e 5 jurados, preencha a matriz com valores fornecidos pelo usuário
e imprima na tela qual o atleta que teve a maior soma de notas entre os jurados
(Imprima a posição da linha do atleta) .
"""
m = [[0 for i in range(5)]for i in range(10)]
for i in range(10):
    for j in range(5):
        m[i][j] = float(input())
r = 0
for l in range(10):
    som = sum(m[l])
    if som > r:
        r = som
        idd = l
print(m[idd], f'posição {idd+1}')
