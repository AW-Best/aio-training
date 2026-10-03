n, capacity_of_water_tank = map(int, input().split())

total = 0
filled_day = 0

for i in range(1, n + 1):
    rain = int(input())
    total += rain

    if total >= capacity_of_water_tank and filled_day == 0:
        filled_day = i


print(filled_day)
