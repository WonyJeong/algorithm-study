import sys
input = sys.stdin.readline
n = int(input())

dp = [0] * 101
dp[1:4] = [1]*3
dp[4:6] = [2]*2
dp[6] = 3

for _ in range(n):
    m = int(input())

    for i in range(6, m+1):
        if dp[i] == 0:
            dp[i] = dp[i-1] + dp[i-5]
    print(dp[m])
