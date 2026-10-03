N = int(input())
ribbon = 0
#1. Write the input correctly
#2. calculate the highest and lowest number in the N digits
#3. Highest - lowest + 1 and then print the answer

numbers = [int(input()) for _ in range(N)]

highest = max(numbers)
lowest= min(numbers)
ribbon = highest-lowest+1
print(ribbon)
