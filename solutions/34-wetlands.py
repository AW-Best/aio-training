months = 8

total = []
for _ in range(months):
  total.append(int(input()))

answer = 0
for value in total:

  answer += value
  if answer <= 10:
    answer = 0
  else:
    answer = answer-10
print(answer)
