for i in range(1, 21):
    n = int(input())
    num = 0
    for i in range(1, n+1):
        num += 1
        print('{} x {} = {}'.format(num, n, n*i))
