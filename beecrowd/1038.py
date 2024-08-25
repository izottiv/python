x, y = map(int, input().split())
if x == 1:
    print('Total: R$ {:.2f}'.format(y*4))
elif x == 2:
    print('Total: R$ {:.2f}'.format(y*4.5))
elif x == 3:
    print('Total: R$ {:.2f}'.format(y*5))
elif x == 4:
    print('Total: R$ {:.2f}'.format(y*2))
elif x == 5:
    print('Total: R$ {:.2f}'.format(y*1.5))
