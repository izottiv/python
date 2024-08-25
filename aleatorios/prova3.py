while True:
    try:
        nm = []
        pa = 0
        n = int(input())
        for i in range(n):
            m, l = map(str, input().split())
            nm.append([int(m), l])
        for j in range(len(nm)):
            for l in range(len(nm)):
                if nm[l][0] == nm[j][0]:
                    if nm[l][1] != nm[j][1]:
                        pa += 1
        print(pa)
    except EOFError:
        break
