li = [13, 24, 2, 1, 41414, 5, 67, 131]
for i in range(len(li)-1):
    for j in range(len(li)-1):
        if li[j] > li[j+1]:
            c = 0
            c = li[j]
            li[j] = li[j+1]
            li[j+1] = c
print(li)
