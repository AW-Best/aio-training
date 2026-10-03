N,K = map(int, input().strip().split())
pre_answer = (N+K)//(K+1)
answer = N-pre_answer
print(answer)
