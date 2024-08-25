li = [4, 1, 2, 3, 4, 5, 63, 131, 13, 2, 3]
for i in range(len(li)//2):
    if li[i] < li[i+1]:
        li[i], li[i+1] = li[i+1], li[i]
print(li)
