how_many_fruits = int(input().strip())
full_moon = 0

while how_many_fruits % 11 != 1:
    how_many_fruits *= 2
    full_moon += 1
print(full_moon, how_many_fruits)
