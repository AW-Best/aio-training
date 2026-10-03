d = int(input())
total = []
answer = 0
for _ in range(d):
  units = int(input())
  total.append(units)

for i in total:
  if i == 0:
    answer += 1
  else:
    answer = 0

print(answer)
