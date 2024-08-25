a = int(input())
b = int(input())
c = int(input())
if a > b and c < a:
    if b > c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b > a and c < b:
    if a > c:
        print(b, a, c)
    else:
        print(b, c, a)
elif c > a and b < c:
    if a > b:
        print(c, a, b)
    else:
        print(c, b, a)
elif c > b and a < c:
    if b > a:
        print(c, b, a)
    else:
        print(c, a, b)
