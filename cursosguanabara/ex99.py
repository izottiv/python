def maior(*num):
    r = num[0]
    print(f'os numeros foram {num}teve {len(num)}')
    for i in range(len(num)):
        if num[i] > r:
            r = num[i]
            idd = i
    print(num[idd])


maior(10, 20, 30, 10, 23, 13131, 1312)
