a = int(input())
b = 0
while a % 2 == 0:
    a = a // 2
    b += 1



    if a % 2 != 0:
        break
print(a, b)
