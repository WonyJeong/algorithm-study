import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

dp2 = [0 for _ in range(N)]
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1

result = [x+y-1 for x, y in zip(dp, dp2)]

print(max(result))
