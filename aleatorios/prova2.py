while True:
    try:
        m, n = map(int, input().split())
        fatorial = fatorial2 = 1
        for i in range(1, m+1):
            fatorial *= i
        for i in range(1, n+1):
            fatorial2 *= i
        if m == 0:
            fatorial = 1
        elif n == 0:
            fatorial2 = 1
        print(fatorial+fatorial2)
    except EOFError:
        break
