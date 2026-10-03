import random
from functools import total_ordering

n = int(input())


minimum = 1000000
maximum = 0
total = 0
for _ in range(n):
    num = int(input())
    if num < minimum:
        minimum = num

    if num > maximum:
        maximum = num

    total += num


mean = total // n


print(minimum, maximum, mean)
