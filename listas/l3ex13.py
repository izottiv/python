soma = 0
produto = 1
while True:
    n = int(input())
    if n <= 0:
        break
    if n % 2 == 0:
        soma += n
    if n % 2 != 0:
        produto *= n
print('soma dos pares =', soma)
print('produto dos impares', produto)
