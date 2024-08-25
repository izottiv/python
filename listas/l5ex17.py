"""Crie uma matriz 10X10 preenchendo com valores aleatórios gerados pelo computador. 
Em seguida, faça um algoritmo que troque os valores da segunda linha com a oitava 
coluna desta matriz"""
from random import randint
t = 10
m = [[randint(0, 1000) for i in range(t)]for i in range(t)]
temp_coluna = [m[l][7] for l in range(t)]  
for l in range(t):
    m[l][7] = m[1][l]  
    m[1][l] = temp_coluna[l]
for ln in m:
    print(ln)
