num2 = 1
n = [num2]
print(num2)
print(num2)
for i in range(1, 19):
    n.append(num2)
    num2 += n[i - 1]
    print(num2)
