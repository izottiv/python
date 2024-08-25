x = y = 1
li = [x, y]
for i in range(1, 19):
    t = x+y
    x = y
    y = t
    li.append(t)
print(li)
